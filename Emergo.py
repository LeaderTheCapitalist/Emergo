import streamlit as st
import requests
import json

# Set up the page
st.set_page_config(
    page_icon="⚠️",
    page_title="Emergo",
)

st.title("⚠️Emergo")
st.caption("Learn how to react in various dangerous situations")

# All scripts cleaned and formatted
scripts = {
    "Earthquake": """
1. Make your house earthquake-ready:
- Move beds away from windows
- Secure heavy furniture and shelves
- Use shatterproof film on glass surfaces
- Install automatic gas shutoff valves
- Keep emergency supplies (food, water, medicine)

2. During an earthquake:
- If indoors: Drop, cover, and hold on
- Protect head and neck under sturdy furniture
- Stay away from windows
- Don't run outside during shaking
- If in bed: Stay there, cover head with pillow

3. Special situations:
- In a car: Pull over, stop, stay inside
- In wheelchair: Lock wheels, cover head
- Outside: Move to open area away from buildings
- Trapped under debris: Don't move, use whistle

4. After the earthquake:
- Expect aftershocks
- Check for injuries and damage
- Turn off gas if you smell leaks
- Listen to emergency broadcasts
- Avoid using phones unnecessarily
""",
    
    "Flood": """
1. Preparation:
- Know your flood risk area
- Build barriers like sandbags
- Waterproof your basement
- Prepare emergency kit (food, water, meds)
- Have bug spray (floods bring pests)

2. When flood warning comes:
- Move valuables to higher floors
- Secure important documents
- Prepare to evacuate if needed
- Fill bathtubs with clean water

3. During flood:
- Don't walk/drive through floodwaters
- Move to highest level of building
- Avoid attics (you could get trapped)
- Never drink flood water (contaminated)
- If swept away: Point feet downstream

4. After flood:
- Wait for official "all clear"
- Beware of electrical hazards
- Clean and disinfect everything
- Throw out contaminated food
- Watch for mold growth
""",
    
    "Landslide": """
1. Warning signs:
- Tilted trees or poles
- New cracks in ground/walls
- Unusual water flow
- Rumbling sounds
- Sudden changes in water levels

2. Preparation:
- Learn evacuation routes
- Prepare emergency kit
- Know community warning systems
- Consider insurance coverage
- Avoid building on steep slopes

3. During landslide:
- Move to second floor if possible
- Take cover under sturdy furniture
- If outside: Run to nearest high ground
- Avoid river valleys/drainage paths
- Watch for debris flows

4. After landslide:
- Stay away from slide area
- Check for injured people
- Report broken utilities
- Watch for additional slides
- Follow official instructions
""",
    
    "Tornado": """
1. Preparation:
- Know warning signs (dark sky, hail, loud roar)
- Identify shelter location (basement or interior room)
- Prepare emergency kit (helmet, shoes, radio)
- Secure outdoor items that could fly away

2. When warning comes:
- Take shelter immediately
- Lowest level, most interior room
- Get under sturdy furniture
- Protect head and neck
- Avoid windows and large rooms

3. Special situations:
- In mobile home: Evacuate to sturdier building
- In car: Drive to nearest shelter if possible
- Outside with no shelter: Lie in ditch, cover head
- At school: Follow drills, avoid gyms/auditoriums

4. After tornado:
- Watch for broken glass/nails
- Check for gas leaks
- Help neighbors if safe
- Listen to officials
- Avoid damaged buildings
""",
    
    "Terrorist Attack": """
1. General preparation:
- Know emergency exits in public places
- Be aware of your surroundings
- Learn first aid basics
- Have emergency contacts saved
- Know local emergency numbers

2. During attack:
- RUN if you can escape safely
- HIDE if you can't escape (lock doors, silence phone)
- FIGHT only as last resort
- Use improvised weapons if needed
- Stay out of open areas

3. Chemical attacks:
- Cover mouth with cloth
- Move upwind if possible
- Seal doors/windows with tape
- Turn off ventilation
- Remove contaminated clothing

4. After attack:
- Follow police instructions
- Avoid crowds/gatherings
- Don't spread unverified info
- Seek counseling if needed
- Report suspicious items
""",
    
    "House Fire": """
1. Prevention:
- Don't leave cooking unattended
- Keep flammables away from heat
- Check electrical wiring
- Test smoke alarms monthly
- Have fire extinguishers

2. Escape plan:
- Know two ways out of every room
- Practice fire drills
- Designate meeting spot outside
- Keep exits clear
- Teach kids how to respond

3. During fire:
- Get out immediately
- Stay low to avoid smoke
- Feel doors before opening
- Use stairs, not elevators
- Stop, drop, roll if clothes catch fire

4. If trapped:
- Seal doors with wet cloth
- Signal from window
- Stay near floor
- Don't hide in closets
- Wait for firefighters
"""
}

# User selects a situation
with st.form("inputs"):
    situation = st.radio("Choose a situation", list(scripts.keys()))
    button = st.form_submit_button("Generate Quiz")

if button and situation:
    # Create the prompt for DeepSeek
    prompt = f"""
    Create a 4-question multiple choice quiz about {situation} safety based on the following information.
    For each question, provide 4 answer choices labeled a) to d) with only one correct answer.
    After all questions, provide the correct answers with brief explanations (1 sentence).

    Format exactly like this:
    
    1. [Question text]
    a) [Option 1]
    b) [Option 2]
    c) [Option 3]
    d) [Option 4]
    
    2. [Question 2...]
    a) [Option]
    b) [Option]
    c) [Option]
    d) [Option]
    
    [Continue for 4 questions]
    
    Correct Answers:
    1. [Correct letter] - [Brief explanation]
    2. [Correct letter] - [Brief explanation]
    3. [Correct letter] - [Brief explanation]
    4. [Correct letter] - [Brief explanation]

    Information to use:
    {scripts[situation]}
    """

    # Make the API call to DeepSeek
    st.subheader(f"{situation} Safety Quiz")
    
    with st.spinner("Generating quiz questions..."):
        try:
            headers = {
                "Authorization": f"Bearer {st.secrets['API']}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 1000
            }

            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )

            if response.status_code == 200:
                api_response = response.json()
                generated_text = api_response['choices'][0]['message']['content']
                
                # Split questions and answers
                parts = generated_text.split("Correct Answers:")
                questions_part = parts[0].strip()
                answers_part = parts[1].strip() if len(parts) > 1 else ""
                
                # Display quiz
                st.markdown("---")
                st.markdown(questions_part)
                
                # Initialize session state for user answers
                if 'user_answers' not in st.session_state:
                    st.session_state.user_answers = {}
                
                # Create form for user responses
                with st.form("quiz_answers"):
                    for line in questions_part.split('\n'):
                        if line.startswith(('1.', '2.', '3.', '4.')):
                            q_num = line.split('.')[0]
                            st.markdown(f"**{line}**")
                        elif line.startswith(('a)', 'b)', 'c)', 'd)')):
                            option = line[0]
                            st.session_state.user_answers[f"q{q_num}_{option}"] = st.checkbox(
                                line, 
                                key=f"q{q_num}_{option}"
                            )
                    
                    submitted = st.form_submit_button("Submit Answers")
                
                # Show answers when submitted
                if submitted:
                    st.markdown("---")
                    st.subheader("Results")
                    
                    # Split answers into individual ones
                    correct_answers = {}
                    for ans_line in answers_part.split('\n'):
                        if ans_line.strip() and ')' in ans_line:
                            q_num = ans_line.split('.')[0]
                            correct_part = ans_line.split(')')[0]
                            correct_answers[q_num] = correct_part.strip()
                    
                    # Evaluate each question
                    score = 0
                    for q_num in ['1', '2', '3', '4']:
                        user_correct = True
                        for option in ['a', 'b', 'c', 'd']:
                            key = f"q{q_num}_{option}"
                            is_correct = (option == correct_answers.get(q_num, '').lower())
                            
                            if st.session_state.user_answers.get(key, False):
                                if is_correct:
                                    st.success(f"Question {q_num}: {option} is correct!")
                                else:
                                    st.error(f"Question {q_num}: {option} is incorrect")
                                    user_correct = False
                        
                        if user_correct:
                            score += 1
                    
                    st.markdown(f"### Score: {score}/4")
                    
                    with st.expander("See all correct answers"):
                        st.markdown(answers_part)
            
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
                st.info("Here's a sample of what would be generated:")
                st.markdown("""
1. What should you do first when you feel earthquake shaking indoors?
a) Run outside immediately
b) Drop to the ground, take cover, and hold on
c) Stand in a doorway
d) Call emergency services

2. Where is the safest place to be during a tornado if you don't have a basement?
a) In a car trying to outrun it
b) In a bathroom or closet on the lowest floor
c) In the attic
d) Under a highway overpass

Correct Answers:
1. b) Drop to the ground, take cover, and hold on - This protects from falling objects.
2. b) In a bathroom or closet on the lowest floor - Small interior rooms offer most protection.
""")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Here's a sample of what would be generated:")
            st.markdown("""
1. If trapped in a burning building, what should you do?
a) Jump out the nearest window
b) Seal doors with wet cloth and signal from window
c) Hide in a closet
d) Run through the flames

2. What's the most important preparation for flood safety?
a) Knowing your evacuation route
b) Buying expensive equipment
c) Waiting until it happens
d) Ignoring weather warnings

Correct Answers:
1. b) Seal doors with wet cloth and signal from window - This prevents smoke entry and helps rescuers locate you.
2. a) Knowing your evacuation route - Preparedness saves lives during floods.
""")

    # Debugging view
    with st.expander("Debug: View API Prompt"):
        st.code(prompt)
