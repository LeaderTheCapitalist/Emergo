import streamlit as st



earthquake_script = """
# 10 Ways to Survive an Earthquake, According to Experts
00:00:01.170 [Music]
00:00:04.700 ten ways to survive an earthquake people
00:00:10.590 who live in an area with a lot of
00:00:12.269 seismic activity really need to know
00:00:14.490 what to do before during and after an
00:00:17.190 earthquake in fact no one is 100 percent safe
00:00:20.939 from this disaster because you never
00:00:22.590 know where you might be traveling or
00:00:24.480 living in the future so pay close
00:00:26.550 attention to these safety
00:00:27.840 recommendations that could save your
00:00:29.640 life one day one make your house your
00:00:36.090 fortress if your region or state has
00:00:40.110 high seismic activity it's better to be
00:00:42.510 prepared for earthquakes if you are not
00:00:44.460 sure how prone to earthquakes your area
00:00:46.590 is you can find this information on
00:00:48.480 special websites like http temblor net
00:00:51.719 arming yourself with this knowledge will
00:00:54.090 help you be aware of possible dangers in
00:00:56.280 the future fortifying your house is a
00:00:58.350 good place to start to do this you
00:01:00.270 should move all the beds away from
00:01:02.670 windows this can save your life if an
00:01:04.979 earthquake occurs at night strengthen
00:01:07.170 shelves so that heavy objects won't fall
00:01:09.450 on you during tremors cover all glass
00:01:12.150 surfaces in your home with special
00:01:14.130 shatterproof film this can save you from
00:01:16.830 serious wounds and bleeding in case of
00:01:19.080 disaster to prevent gas and water leaks
00:01:21.869 get an automatic shutoff device or a
00:01:24.270 main switch so that you can quickly kill
00:01:26.400 the gas and power in the entire house
00:01:28.350 keep extra fire extinguishers batteries
00:01:31.350 flashlights and emergency food supplies
00:01:33.780 in your home
00:01:34.590 always store necessary medicines in your
00:01:37.229 medicine cabinet have an expert test
00:01:39.479 your houses foundation so it won't slip
00:01:41.700 during an earthquake get earthquake
00:01:44.009 insurance for your home this will really
00:01:46.350 help you out after a disaster
00:01:50.800 if you're in a building if you're in
00:01:57.020 some building and you feel the place
00:01:58.730 vibrating see falling objects or here
00:02:01.190 glass breaking don't panic stay calm and
00:02:04.340 try to reassure others never leave the
00:02:07.040 building during an earthquake the second
00:02:09.680 you feel the tremors of an earthquake
00:02:11.000 drop cover and hold on drop right where
00:02:15.530 you are on to your hands and knees this
00:02:17.570 is a safe position that allows you to
00:02:19.550 slowly move toward shelter use one arm
00:02:22.670 to cover your head and neck
00:02:24.380 a massive desk or table makes a good
00:02:26.780 shelter if there's nothing in the room
00:02:28.850 to hide under at least stay away from
00:02:31.070 the windows
00:02:32.000 remain in this position and bend over as
00:02:34.580 much as you can to protect your vital
00:02:36.470 organs hold on like this until the
00:02:39.380 shaking stops
00:02:40.430 if you are able to find some shelter
00:02:42.320 hold on to it using one hand and be
00:02:44.840 prepared to move with it as it might
00:02:46.730 shift do you get it now drop cover and
00:02:50.150 hold on
00:02:51.110 learn this rule by heart it could save
00:02:54.110 your life
00:02:58.060 3 if you're outside
00:03:02.240 be ready to help people in case you're
00:03:04.580 out in the middle of disaster during the
00:03:06.650 tremors don't enter buildings and don't
00:03:09.260 run around them stay outside move away
00:03:12.380 from power lines tall buildings and
00:03:14.720 roads try to find shelter and hide and
00:03:17.210 again drop cover and hold on for if
00:03:25.010 you're in a car being in a car during an
00:03:30.080 earthquake is really dangerous panic on
00:03:32.660 the road can turn into a serious
00:03:34.370 accident so remember to slow down and
00:03:36.980 find a safe place to stop the car
00:03:38.840 preferably the curb avoid powerlines and
00:03:41.990 high-rise buildings don't get out of the
00:03:44.900 car until the earthquake stops five if
00:03:51.680 you're on the beach or near the shore if
00:03:54.490 you feel the shocks
00:03:56.510 somewhere by the water don't wait around
00:03:58.460 to be told what to do an earthquake can
00:04:00.920 trigger a tsunami so it's better to
00:04:03.170 collect your things immediately and move
00:04:05.930 to higher ground six if you're in a
00:04:12.590 wheelchair in case you're in a
00:04:15.770 wheelchair and you see and feel an
00:04:17.600 earthquake starting look around for
00:04:19.399 shelter try to get there as fast as you
00:04:21.950 can then lock your wheels cover your
00:04:25.790 head and neck with your hands and
00:04:27.380 anything else available like a book rug
00:04:29.840 or pillow and hold on to something
00:04:32.480 sturdy
00:04:33.380 so remember lock cover and hold on if an
00:04:37.850 earthquake has never occurred in your
00:04:39.470 city there are online resources where
00:04:41.810 you can read the public recommendations
00:04:43.700 for people using a cane walker or
00:04:45.800 wheelchair this website for instance has
00:04:48.560 some important information on the matter
00:04:51.250 WWF quake country org slash disability
00:04:57.860 [Music]
00:04:59.440 seven if you were in a stadium if
00:05:03.490 watching your favorite team at the
00:05:05.720 stadium has suddenly been interrupted by
00:05:07.640 an earthquake stay where you are never
00:05:10.250 start a panic in a crowd instead get on
00:05:13.550 the floor in the space in front of your
00:05:15.380 seat bend over and cover your head and
00:05:17.630 neck with your hands stay calm and
00:05:20.300 reassure others eight if you are in an
00:05:26.630 elevator if you're thinking about using
00:05:31.610 the elevator to get out of the building
00:05:33.020 during an earthquake think again stay in
00:05:35.840 the building or use the stairs if
00:05:37.460 necessary the fact is that electricity
00:05:39.980 during an earthquake is unstable and can
00:05:42.230 easily go out if you're caught unaware
00:05:44.450 in the elevator then take the following
00:05:46.250 actions lie down on the floor cover your
00:05:49.490 head with your hands wait until the
00:05:51.620 elevator starts working again get out on
00:05:54.110 the next floor and use the stairs 9 if
00:06:01.010 you are in bed sometimes earthquakes
00:06:05.570 happen at night if you've woken up by
00:06:07.550 the room shaking and realize there's an
00:06:09.500 earthquake happening try to do the
00:06:11.180 following stay in bed protect your head
00:06:13.820 with a pillow and lie face down if
00:06:15.890 there's a shelf above your bed or a
00:06:18.020 ceiling lamp that can fall on your head
00:06:19.820 then move to a safe place 10 if you're
00:06:27.290 trapped under rubble if by any chance
00:06:31.370 during or after an earthquake you become
00:06:33.830 trapped and can't get out from beneath
00:06:35.450 debris and rubble here's what you should
00:06:37.520 do to survive don't move
00:06:39.890 it'll just kick up dust and can get in
00:06:42.080 your eyes and lungs cover your mouth
00:06:44.180 with a cloth or piece of clothing don't
00:06:46.790 light a lighter or matches don't shout
00:06:49.730 it can be dangerous because of dust if
00:06:52.280 you have a whistle use it so that
00:06:54.470 rescuers can find you if you don't have
00:06:56.900 one
00:06:57.320 see if there's a pipe nearby you can
00:06:58.970 knock on to alert them
00:07:02.120 that finishes off our list but don't go
00:07:05.009 anywhere just yet it's crucial that you
00:07:07.410 always keep in mind some general rules
00:07:09.479 for evacuation overall evacuation rules
00:07:19.580 evacuation is one way to protect people
00:07:22.169 in case of natural disasters major
00:07:24.180 industrial accidents and disasters if
00:07:26.699 you've received a notification that an
00:07:28.830 evacuation has started you should close
00:07:31.289 all windows and shut off the gas water
00:07:33.630 and electricity in your homes
00:07:35.220 immediately collect only necessary
00:07:37.440 things and exit the building in a calm
00:07:39.780 and organized manner through the
00:07:41.370 emergency exits after leaving the
00:07:43.889 building find a safe place if you can't
00:07:46.860 leave the building find a table and drop
00:07:49.530 cover and hold on if you're trapped
00:07:52.530 don't panic try to get your bearings and
00:07:55.199 give signals about your location don't
00:07:57.720 shout
00:07:58.500 knock or bang on metal slabs or pipes
00:08:01.070 remember that the first shocks are the
00:08:03.479 strongest from 5 to 40 seconds after
00:08:06.479 that there may be a temporary lull and
00:08:08.729 then another push if you have any tips
00:08:15.330 you'd like to add to this list please
00:08:17.070 tell us in the comments and we'll be
00:08:18.750 sure to highlight your useful advice
00:08:20.460 share this video with your family and
00:08:22.680 friends to help them stay safe in case
00:08:24.750 of an emergency and give it a like so
00:08:26.789 that more people will see it if you're
00:08:28.440 new here subscribe to our channel so
00:08:30.419 that you won't miss any of our important
00:08:32.130 updates stay with us on the bright side
00:08:34.529 of life
00:08:35.460 [Music]
"""

flood_script = """
# tactiq.io free youtube transcript
# How to Survive a Flood
# https://www.youtube.com/watch/rV1iqRD9EKY

00:00:09.542 Heavy rain has been coming down for days
00:00:12.145 and it won't let up.
00:00:14.247 A loud crash outside catches your attention.
00:00:17.150 You look out the window.
00:00:18.818 A massive surge of water is sweeping away
00:00:21.888 trees, cars, and buildings with ease.
00:00:25.859 A flash flood has overrun your town.
00:00:29.529 The floodwater bursts open your door
00:00:32.098 and starts rushing into your house.
00:00:35.969 Hold your breath, because
00:00:43.043 You might think that hurricanes
00:00:44.944 or earthquakes top the list
00:00:46.713 of the deadliest natural disasters.
00:00:48.915 But floods are one of the most common,
00:00:51.217 most destructive,
00:00:53.486 and most deadly natural disasters in the world.
00:00:57.524 Floods happen when water
00:00:59.626 overflows onto dry land.
00:01:01.761 This can be caused by heavy rain,
00:01:04.197 ocean waves, or when a dam breaks.
00:01:08.468 They're frequent in coastal areas,
00:01:10.770 floodplains, and areas near a river or stream.
00:01:15.442 And with rising sea levels
00:01:17.110 and heavier rainfall due to climate change,
00:01:20.747 the number of floods is
00:01:22.182 projected to increase drastically.
00:01:42.335 First things first.
00:01:43.403 Protect yourself and your property.
00:01:45.805 If you live in an area that's prone to flooding,
00:01:48.274 one of the best things you can do to prepare
00:01:50.610 is to make your house flood proof.
00:01:53.480 Feeling handy?
00:01:54.614 You can fortify your house by 
00:01:56.649 constructing a barrier to stop the floodwater.
00:02:00.520 Building levees, floodwalls,
00:02:02.922 or piling up sandbags
00:02:04.424 can help keep the water out.
00:02:06.493 If the flood breaks through the barriers,
00:02:09.027 the first place it'll reach is your basement.
00:02:12.398 Sealing the basement walls
00:02:13.967 with a waterproofing coating
00:02:15.635 can help to avoid seepage and damage.
00:02:19.005 Okay, now that you've prepared your house,
00:02:21.741 what should you do to prepare yourself?
00:02:29.115 When a flood happens,
00:02:30.917 chances are you won't be able to head out 
00:02:33.219 for a peaceful stroll to the grocery store.
00:02:36.289 So stock up on emergency supplies
00:02:38.892 ahead of time.
00:02:40.627 Buy plenty of bottled water,
00:02:42.629 nonperishable food, flashlights,
00:02:45.131 and a first aid kit.
00:02:47.000 Oh, and pack a bottle of bug spray too.
00:02:50.103 Floods don't just force people out of their homes.
00:02:53.239 All kinds of bugs and pests will be
00:02:55.942 flooded out of their habitats and into yours. 
00:03:02.448 Looks like a flood's on its way. Get ready.
00:03:12.759 A flood warning is in effect.
00:03:14.594 That means a flood is about to happen,
00:03:17.197 or is already happening.
00:03:19.699 Gather all your valuables, like your computer,
00:03:22.435 phone, important documents, and your pets.
00:03:26.739 Move them to a higher floor
00:03:28.474 where they're less likely to be
00:03:30.109 damaged or lost in the flood.
00:03:33.146 If you don't have an upper level,
00:03:35.281 try to get your belongings
00:03:37.150 somewhere  high and safe,
00:03:38.284 like a family member or friend's home.
00:03:41.621 Water starts seeping through 
00:03:43.289 the cracks of your house.
00:03:44.857 It's rising fast. What should you do now?
00:03:55.001 If you're at home, don't go downstairs.
00:03:58.104 Instead, get to a higher level above the water.
00:04:01.274 But don't hide in the attic.
00:04:03.176 Since most attics only have one way
00:04:05.478 to get in or out,
00:04:06.913 you could easily get trapped in there.
00:04:10.650 If you forgot something in the flood,
00:04:12.352 or are thinking about walking through
00:04:14.320 a flooded area, don't.
00:04:16.856 It'll be hard to determine how deep the water is,
00:04:20.360 and what kinds hazards lie below.
00:04:23.529 And whatever you do, don't drink tap water, 
00:04:26.699 and especially don't drink the flood water.
00:04:30.236 "It's a bit nutty."
00:04:32.138 It could be contaminated with sewage,
00:04:34.607 gasoline, or bacteria.
00:04:37.377 Stick to your bottled water.
00:04:40.146 The rain's unrelenting.
00:04:41.748 The flood's still rising.
00:04:43.549 Forget your belongings.
00:04:45.018 Your last resort is to get on the roof
00:04:47.487 and call for help.
00:04:49.522 But the wind is strong,
00:04:51.824 and an unsuspecting wave
00:04:53.459 pushes you into the water.
00:04:59.565 You're caught in the fast moving flood.
00:05:02.769 Do everything possible to
00:05:04.337 keep your feet pointed downsteam
00:05:07.073 and move over obstacles.
00:05:09.776 Then, try to grab or climb onto anything
00:05:12.812 that can keep you stable or above the water.
00:05:17.016 Once you've got ahold of something,
00:05:18.451 yell for help, as loudly as possible.
00:05:26.025 You caught a lucky break.
00:05:27.794 A rescue team saved you,
00:05:29.395 and the flood died down.
00:05:31.597 But don't get settled just yet.
00:05:34.200 You've got some cleaning up to do.
00:05:36.502 Everything in your home that was
00:05:38.171 in contact with the floodwaters
00:05:39.839 could be contaminated.
00:05:41.908 Remember, the water may have been
00:05:43.509 polluted with sewage and diseases.
00:05:46.879 Once your house is dry and clean,
00:05:49.515 take a rest. You survived a flood.
00:05:53.419 But what if the heavy rain causes a landslide?
"""

landslide_scrip = """
# tactiq.io free youtube transcript
# How to Survive a Landslide
# https://www.youtube.com/watch/9j_StYqR_Pg

00:00:09.976 You're out on the balcony, 
00:00:11.544 soaking up the stunning views
00:00:13.546 of the valley's hills.
00:00:16.116 All of a sudden,
00:00:17.083 a violent storm starts to form.
00:00:20.387 You notice the trees along the mountain
00:00:22.956 swaying and falling in the wind.
00:00:25.959 The collapsing forest quickly turns into
00:00:28.828 an enormous wave of trees, dirt, and debris.
00:00:32.732 Don't stand your ground.
00:00:34.267 A landslide is destroying everything in sight.
00:00:37.637 And this one's heading straight for you.
00:00:46.179 A landslide is the movement of soil,
00:00:49.015 rocks, or other types of debris down a slope.
00:00:53.086 Landslides may not look as massive as
00:00:55.588 earthquakes or tsunamis,
00:00:57.524 but they can be just as devastating.
00:01:00.794 About 4.8 million people were affected
00:01:03.997 by landslides in the last 20 years.
00:01:07.434 But, not all landslides are the same.
00:01:10.904 Rockfalls are barrages of loose rock
00:01:14.040 that tumble down steep slopes.
00:01:17.143 They can be caused by
00:01:18.445 earthquakes and mining.
00:01:20.980 Their size can range from teeny tiny pebbles
00:01:24.451 to huge, hulking boulders.
00:01:27.854 Mudslides happen when dirt and debris
00:01:30.757 become saturated with water.
00:01:33.259 Mudslides are often caused by
00:01:34.928 heavy rain or volcanic activity.
00:01:38.231 They can be a slow, creeping sludge,
00:01:40.900 or a fast, all-consuming wave.
00:01:57.717 Like in most natural disasters,
00:01:59.719 you'll have the best chance of surviving
00:02:01.621 if you prepare in advance.
00:02:04.491 Have an emergency kit ready with
00:02:06.326 food, water, flashlights, first aid supplies,
00:02:09.996 and emergency blankets.
00:02:12.098 You'll also want to create and practice
00:02:15.268 an evacuation plan. 
00:02:17.170 Identify all the escape routes
00:02:19.105 from your home and workplace.
00:02:21.141 Choose a meeting spot in case
00:02:23.009 you get separated from family and friends.
00:02:25.812 You may only have minutes
00:02:27.180 to get out of your home.
00:02:32.352 If you live by a mountain or hilly terrain,
00:02:35.221 you could be at risk of a landslide,
00:02:37.657 so listen up.
00:02:40.059 Look for tilted trees, new holes,
00:02:43.163 or bare spots along the hillside.
00:02:46.432 Listen for sounds like rumbling
00:02:48.434 or trees cracking.
00:02:50.436 And pay attention,
00:02:52.005 especially if the authorities are
00:02:53.840 telling you to evacuate.
00:02:55.808 If you think there's a risk of a landslide,
00:02:58.311 don't even think about getting some shut-eye.
00:03:00.947 Be on the alert and stay awake.
00:03:03.716 Most landslide deaths occur
00:03:05.618 when people are sleeping.
00:03:07.987 But it's too late to run.
00:03:10.323 The landslide is right outside your doorstep.
00:03:17.564 If you can see a landslide moving towards you,
00:03:20.166 chances are you probably can't outrun it.
00:03:23.236 Stay inside, and move upstairs
00:03:25.738 or onto higher ground.
00:03:27.640 Then, hunker down underneath
00:03:30.076 some sturdy furniture and wait it out.
00:03:32.845 Getting to a higher spot can help you
00:03:34.881 stay out of the path of the landslide.
00:03:37.817 But what can you do if you're
00:03:39.719 caught outside during a landslide?
00:03:42.755 Don't hide behind a tree or anything unstable.
00:03:46.192 Landslides can be strong enough
00:03:48.061 to push them onto you.
00:03:50.029 Find any possible structures
00:03:51.898 you can hide in to protect you from the debris.
00:03:55.535 Look. Hide over there.
00:03:57.136 You start running towards
00:03:58.304 the building closest to you and
00:04:00.740 uh-oh.
00:04:05.745 With no shelter close by
00:04:07.947 and nothing to climb on,
00:04:09.549 your last resort is to brace yourself.
00:04:12.752 If you have an emergency blanket,
00:04:14.487 cover yourself with it to protect your body
00:04:17.257 Then, curl up in a ball,
00:04:19.192 protect your head from debris,
00:04:21.327 and avoid inhaling water.
00:04:24.030 Luckily, if you are caught in a landslide,
00:04:26.799 there's a chance you won't be
00:04:28.368 buried completely.
00:04:30.236 Once the flow stops,
00:04:31.804 the dirt might be loose enough
00:04:33.873 that you can dig yourself out.
00:04:36.609 The dust has settled,
00:04:38.011 and the landslide has come to a halt.
00:04:40.446 Congratulations, you've survived
00:04:43.116 a catastrophic landslide.
00:04:45.351 Unfortunately, the landslide carried you
00:04:48.588 all the way to the middle of a forest.
00:04:52.859 Where are we? How do we get out?
"""

tornado_script = """
# tactiq.io free youtube transcript
# How to Survive a Tornado And Recognize It
# https://www.youtube.com/watch/wcTdLnrxznM

00:00:00.350 The furious winds of a hurricane, impenetrableblizzards, or the stifling heat of a drought
00:00:09.710 – these are horrible manifestations of nature’swrath – also known as Bad Weather!
00:00:16.289 But not many of them can compare to the fastestwinds in the world.
00:00:20.540 Whirling up high, turning fields into wastelands,tearing trees out from the ground, and ruining
00:00:25.590 towns – that’s right: tornados.
00:00:28.940 More Bad Weather.
00:00:30.430 Still, survivalists say that anyone can preparefor a twister!
00:00:34.190 So let’s find out how to survive a tornado!
00:00:37.339 The first and most important thing any experiencedweatherman, survivalist or tornado chaser
00:00:42.899 will tell you is you need to know what you’redealing with.
00:00:46.960 Without a clear understanding of what exactlya tornado is, every other tip or piece of
00:00:51.659 advice has a good chance to fall flat anddo no good after all.
00:00:56.399 A tornado can emerge even when there’s nostorm or rain.
00:01:00.149 It comes without knocking; and its formationis sudden and quick.
00:01:04.319 It might take only a few minutes before atornado starts to wreak havoc upon everything
00:01:08.960 in its path.
00:01:10.659 Most of the time they appear in the summerwhen the ground is heated and the upper parts
00:01:14.780 of the atmosphere are influenced by cold windsbrought on by thunderstorm supercells.
00:01:20.100 The hot air tends to produce updrafts – anascending stream of warm air.
00:01:24.610 At the same time, thunderstorms bring rainand a descending stream of cold air called
00:01:29.840 a downdraft.
00:01:31.170 As you can imagine, these two rapid airstreamscolliding with each other isn’t a great
00:01:35.899 thing for anyone.
00:01:37.700 Warm air can’t flow higher up and cold aircan’t go lower.
00:01:41.450 The force of their collision creates a spinningwall cloud right below the level of the parenting
00:01:47.050 storm.
00:01:48.050 With time, both the updraft and the downdraftbecome stronger and stronger.
00:01:52.700 It eventually produces a vertical column ofspinning air that starts to suck debris from
00:01:57.450 the ground like a giant drain.
00:01:59.679 This is when the funnel of a tornado appearsfrom the spinning wall cloud.
00:02:04.039 It makes its way down from the cloud to theground as if the storm itself tries to suck
00:02:08.690 up the earth with a long weird snout.
00:02:10.889 And it won’t shy away from taking everythingfor a ride.
00:02:15.230 The force of the thing is immense.
00:02:17.380 Just try to imagine: a tornado can be up to2 miles in diameter.
00:02:22.000 The wind speed sometimes surpasses 300 mph,and the speed of the funnel itself traversing
00:02:28.030 the land is somewhere between 25 to 40 mph;but in some cases, it can reach 70 mph.
00:02:36.520 You wouldn’t want to race with somethinglike that, and it’s certainly not a welcome
00:02:40.220 guest in your back yard.
00:02:42.100 But what can you do to avoid meeting a twister?
00:02:45.170 The main way to assure your safety is to beaware of your surroundings, and plan in case
00:02:50.230 a tornado comes your way.
00:02:52.490 Most tornadoes happen in a warmer time ofyear, and their favorite place on Earth must
00:02:57.120 be the US.
00:02:58.120 In fact, there’s even a term: ‘TornadoAlley’, which includes most of the Southeastern
00:03:03.510 and Midwestern parts of the country.
00:03:05.810 But don’t think that you’re safe outsideof these regions!
00:03:08.950 Believe it or not, tornadoes have appearedin the middle of winter, and in the least
00:03:12.970 obvious places.
00:03:15.260 Meteorologists are still working hard on gainingmore knowledge about tornadoes and the origins
00:03:19.510 of their formation.
00:03:21.300 Considering a warning is your best chanceat survival, it’s a good thing they figured
00:03:25.570 out how to predict them for the most part.
00:03:28.300 And more than that, you too could become atornado spotter.
00:03:32.370 These are specially trained people that candetect the very first signs of a storm that
00:03:36.360 can produce a tornado.
00:03:38.210 There are more than 230,000 of these vigilantstorm-watchers across the US.
00:03:43.600 Their main task is to see if the storm isa supercell producing a wall cloud.
00:03:48.140 They’re not really hard to see: it lookslike a giant bulge in the cloud base that
00:03:53.420 starts to spin as an updraft from the groundstrikes it.
00:03:57.170 The moment they see a wall cloud startingto split into bands called ‘beaver tales’,
00:04:02.310 they know that they’re looking at the birthof a tornado.
00:04:05.660 But how do they know which way to look?
00:04:08.090 This is where technology comes into play.
00:04:11.860 Meteorologists use weather radar, which isbased on the Pulse-Doppler method.
00:04:16.029 Pulse-Doppler radars can detect raindropsand effectively calculate the distance to
00:04:20.660 them and their velocity.
00:04:22.750 Based on that information, meteorologistscan form a full picture of changes in the
00:04:27.070 weather.
00:04:28.070 The same radars can detect rotation in stormclouds from more than 160 miles away.
00:04:34.060 When observers confirm the first signs ofupcoming tornadoes, the emergency warning
00:04:38.810 will immediately go off.
00:04:40.810 You would need to sit in a bunker to missthis one, because it’ll be literally everywhere.
00:04:46.090 Speaking of bunkers, you would probably beglad to have one nearby, or at your own disposal,
00:04:51.720 if you’re about to weather something likean F-3 category tornado.
00:04:55.810 And there are 6 of these categories, so youcan imagine what you’re up against with
00:04:59.880 anything stronger than an F-3.
00:05:02.560 If you still can’t, here’s a quick rundownfor you.
00:05:11.250 An F-0 tornado is more like a landspout – itwon’t cause any significant damage.
00:05:16.420 To be safe you would need to just trim thetree branches closest to your windows so they
00:05:21.430 won’t break them.
00:05:22.520 Otherwise, your home is your castle.
00:05:24.760 An F-1 tornado, with wind speeds up to 110mph, is more of a concern.
00:05:30.550 Hope you don’t live in a mobile home; andif you do – find another place to hide.
00:05:36.430 Tornadoes this strong can easily push a mobilehome off its foundation.
00:05:40.200 An F-2 tornado can tear small trees out fromthe ground.
00:05:45.050 Any mobile home would be destroyed by it.
00:05:47.640 Even the roofs of well-constructed houseswill partially crumble under the furious wind,
00:05:52.580 blowing at 160mph.
00:05:54.390 An F-3 tornado is where the real trouble begins.
00:05:59.139 The wind speed can get up to 205 mph.
00:06:02.889 All the upper parts of houses are in danger,and any debris caught by the wind become lethal
00:06:08.360 weapons.
00:06:09.370 These tornadoes can lift cars and break brickwalls.
00:06:12.650 F-4 and F-5 tornadoes are the rarest, butalso the most dangerous.
00:06:18.360 If you ever hear that something like thatis coming your way – it’s best to find
00:06:22.340 a bunker, safe room, or an underground shelternearby.
00:06:26.830 These monstrosities can make buildings literallycome off the ground, and cars fly in the air
00:06:32.500 for 300 ft.
00:06:34.370 Fortunately, there are a lot of shelters thatare specifically built to protect anyone from
00:06:38.600 tornadoes and storms; and you don’t reallyneed to have a personal one for yourself.
00:06:43.639 But what would be nice to have is an emergencykit, just in case.
00:06:47.770 The most useful things for a survival kitwould be rain gear, flares, a radio, a first-aid
00:06:53.750 kit, an air horn, a flashlight with some extrabatteries, a mechanical can opener, at least
00:06:59.870 3 gallons of water per person, a stock ofready to eat meals, and some walkie-talkies.
00:07:05.790 Make a stash with all of that somewhere inyour house, and you’ll always be prepared.
00:07:11.340 The worst-case scenario is if a tornado catchesyou off guard.
00:07:15.790 Imagine you’re driving a car and suddenlya twister appears in front of you from a huge
00:07:20.650 raincloud.
00:07:21.870 What would you do then?
00:07:23.400 The first thing that comes to mind is to justturn around and drive away from it as fast
00:07:28.190 as possible, but, that’s a poor choice ofactions.
00:07:31.730 The best way to avoid a tornado in a car isto figure out the direction it’s going and
00:07:36.520 take a course about 90 degrees from this direction.
00:07:40.200 But remember, if it is close to you – don’tthink that your car will protect you.
00:07:44.620 It’s not only the wind that’s scary abouta tornado.
00:07:47.979 More so are the debris that it spins around;it could severely damage your car in a matter
00:07:52.790 of seconds.
00:07:53.790 It’s best to leave the car and stay as faraway from it as you can.
00:07:58.210 In this worst-case scenario, your best optionis to find a ditch, lay low, and cover your
00:08:03.570 head with any possible means.
00:08:05.810 Still, any nearby building’s basement wouldbe a better hiding place, except the big ones.
00:08:11.340 Shopping malls or cinemas could be extremelydangerous if you want to hide from tornadoes.
00:08:16.419 The myth that larger structures are saferis just a myth.
00:08:21.370 And that’s not the only myth about twisters.
00:08:24.030 Telling them from the truth may be crucialfor surviving a disaster.
00:08:28.300 One suggests that it’s better to open windowsduring a tornado, and that’s as false as
00:08:32.909 it gets.
00:08:34.339 Wind going through open windows could liftwhole floors or a roof with ease!
00:08:38.849 More than that – it’s important to leavewindows closed and to stay away from them
00:08:43.110 until the whirlwind is no more.
00:08:45.670 Another important misconception is that smallertornados are weaker and less dangerous.
00:08:50.459 That’s also not true.
00:08:52.459 A lot of F-4 tornadoes were no wider thanjust 300 ft in diameter, but they did a ton
00:08:58.630 of damage.
00:08:59.630 Twisters aren’t stable, they change theirshapes constantly.
00:09:03.529 So don’t just trust your eyes – all tornadoesare equally dangerous.
00:09:08.519 No matter how small or slow-looking a twisteris – try to not underestimate it, and always
00:09:14.209 use every method of avoiding trouble.
00:09:17.949 How about you?
00:09:19.020 Have you ever seen a real tornado?
00:09:21.279 Let me know down in the comments!
00:09:23.170 If you learned something new today, then givethis video a like and share it with a friend.
00:09:27.709 But – hey! – don’t go flopping intoa ditch just yet!
00:09:31.230 We have over 2,000 cool videos for you tocheck out.
00:09:34.749 All you have to do is pick the left or rightvideo, click on it, and enjoy!
00:09:39.250 And remember: Stay on the Bright Side of life!
"""

terrorist_script = """
# tactiq.io free youtube transcript
# How to Prepare in Case of a Terrorist Attack | Disasters
# https://www.youtube.com/watch/hs2prs9xVk8

00:00:02.120 [Music]
00:00:10.840 in this video you'll learn how to act
00:00:12.559 appropriately in a case of a terrorist
00:00:15.920 attack if you hear the civil defense
00:00:18.199 siren or other public warning system
00:00:20.560 seek immediate shelter in an enclosed
00:00:23.000 space be aware a car is not a good
00:00:25.720 hiding place if you're in one get out
00:00:28.920 and enter the nearest building
00:00:31.000 building seal any gaps in all doors
00:00:34.120 windows and vents with wet cloth or
00:00:36.440 adhesive tape to stop the outside air
00:00:38.600 from
00:00:42.280 entering turn off any ventilation air
00:00:45.360 conditioning or Central Heating switch
00:00:48.160 off the gas supply at the
00:00:51.359 mains listen to the National radio and
00:00:54.079 follow their
00:00:56.840 instructions use your phone as little as
00:00:59.239 possible to eat Network
00:01:01.960 congestion do not light any Flames do
00:01:04.959 not smoke and do not flick any switches
00:01:07.400 as these could cause
00:01:09.190 [Music]
00:01:10.840 explosions do not go to collect your
00:01:13.119 children from school the teachers who
00:01:15.520 have received special training for these
00:01:17.600 situations will look after them if
00:01:20.360 you're caught up in a chemical
00:01:22.960 attack protect your eyes nose mouth and
00:01:26.520 other exposed areas with a damp cloth if
00:01:29.200 possible
00:01:34.520 get as far away as you can from the
00:01:36.040 sight of the attack but without running
00:01:38.200 in order to keep your breathing and
00:01:39.640 heart rate
00:01:42.479 normal but do not go too far from the
00:01:44.960 affected area so that you can receive
00:01:47.159 treatment from Emergency Services who
00:01:49.159 will be on their way do not use your
00:01:51.880 phone as this may overload the telephone
00:01:55.560 network if a liquid or powder from an
00:01:58.320 envelope or package has got on your
00:02:00.479 person put it in a plastic bag being
00:02:03.360 careful to touch as little as possible
00:02:05.680 also seal the bag in the most airtight
00:02:07.960 way
00:02:11.319 possible alert the authorities and
00:02:13.560 follow their
00:02:16.200 instructions switch off the ventilation
00:02:18.519 system
00:02:20.640 immediately close all doors and Evacuate
00:02:23.239 the
00:02:25.120 premises take off your clothes put them
00:02:27.680 in a plastic bag and seal it tight
00:02:33.440 wash the parts of your body that came
00:02:35.200 into contact with a
00:02:36.879 substance do not drink do not eat do not
00:02:40.440 smoke and do not touch anyone
00:02:44.560 else wait for the Emergency Services to
00:02:48.400 arrive if you find yourself at the sight
00:02:50.920 of a terrorist attack try to
00:02:54.239 escape get as far away as possible from
00:02:56.879 danger and help those nearby
00:03:00.140 [Music]
00:03:01.760 if you cannot Escape
00:03:05.080 hide lock yourself in
00:03:07.879 door switch off the lights and turn off
00:03:10.560 any electric devices creating noise step
00:03:13.760 away from openings such as doors and
00:03:15.879 windows and lie on the
00:03:17.840 floor or else seek shelter behind a wall
00:03:20.879 or
00:03:22.959 pillar stop your phone from ringing or
00:03:27.319 vibrating alert the Police and listen to
00:03:30.040 their directions approach them with your
00:03:32.599 hands raised and your palms showing
"""

fire_script = """
# tactiq.io free youtube transcript
# How To Survive A House Fire ? | Fire Safety Education for Kids | The Dr Binocs Show | Peekaboo Kidz
# https://www.youtube.com/watch/Xgc90CoJbDI

00:00:00.539 foreign
00:00:05.700 [Music]
00:00:14.780 thank goodness it's just you little
00:00:17.640 kitty I thought something got fire
00:00:24.300 D well right now it's just a pretend
00:00:28.019 situation but if a fire happens in real
00:00:31.260 life it can be really dangerous that's
00:00:34.800 why we need to learn some necessary
00:00:37.200 things to keep ourselves and our loved
00:00:40.379 ones safe
00:00:42.260 let me answer that by sharing a fiery
00:00:46.020 question how to survive a fire zoom in
00:00:50.760 thank you
00:00:52.320 won't believe it but in less than 30
00:00:55.739 seconds a small spark can quickly grow
00:00:58.680 into a raging fire that eats up
00:01:01.800 everything in its spot your toys books
00:01:05.939 furniture and even the walls also it's
00:01:11.100 not just the Flames to be worried about
00:01:13.220 but also the toxic smoke coming from the
00:01:17.159 fire is thick and dangerous which can
00:01:20.759 make it hard to breathe and see and as
00:01:24.780 it can happen to anyone anywhere and
00:01:27.960 anytime let us see a few safety
00:01:31.500 techniques to survive this
00:01:33.799 life-threatening situation
00:01:37.159 firstly as they say prevention is better
00:01:40.740 than cure
00:01:42.380 so make sure not to touch objects like
00:01:46.020 matches lighters and candles if there
00:01:49.500 are no adults around and in case the
00:01:52.380 situation demands you to do so then do
00:01:56.040 not take them anywhere near flammable
00:01:58.619 items such as cartoons clothing and
00:02:02.159 bedding
00:02:03.259 and always remember to turn off and
00:02:07.079 unplug appliances when you're not using
00:02:10.139 them to prevent short circuits
00:02:13.680 but in case a fire does break out the
00:02:17.459 first thing you should do is try to stay
00:02:20.099 calm and not panic so that you can think
00:02:23.340 clearly then immediately call for
00:02:26.819 firefighters and alert everyone in the
00:02:29.819 house or school and if there is no easy
00:02:33.120 Escape Route and you see the toxic smoke
00:02:36.180 filling up the space then quickly soak a
00:02:39.420 cloth in water and tie it over your
00:02:42.300 mouth and nose as breathing in too much
00:02:45.239 smoke can cause you to pass out
00:02:49.200 also as this smoke tends to rise up to
00:02:53.340 give yourself some extra time quickly
00:02:55.860 get on your hands and knees and crawl
00:02:58.379 towards the nearest exit and if you're
00:03:01.500 in a room and the door is closed check
00:03:04.620 to see if it's hot before opening it if
00:03:08.879 it's hot this means there's a fire on
00:03:12.060 the other side and you should try to
00:03:14.400 find another way out if the dough is
00:03:17.819 cooled then open it slowly and check for
00:03:20.700 smoke or flames and move ahead by
00:03:23.760 staying low
00:03:26.040 and if you're trapped in a room and
00:03:28.980 can't get out try to seal the room off
00:03:32.159 as much as possible stuffed clothes or
00:03:35.519 towels under the door to stop smoke from
00:03:38.879 coming in and seal any gaps around the
00:03:42.360 window with wet towels or sheets
00:03:45.980 and by any chance someone's clothes
00:03:49.319 happen to catch fire then use a safety
00:03:53.099 technique called stop drop and roll
00:03:57.680 According to which the first thing to do
00:04:00.420 is to stop moving drop to the ground and
00:04:04.200 cover your face with your hands that
00:04:06.659 roll over and over until the Flames are
00:04:09.840 extinguished and once you are out of the
00:04:12.599 toxic smog Zone
00:04:14.459 quickly get out of the place and leave
00:04:17.279 the rest to the professional
00:04:18.720 firefighters
00:04:20.839 and most importantly help your loved
00:04:24.360 ones by sharing this video and let us
00:04:27.360 know how many people you shared it with
00:04:29.580 by emailing us at peekaboo kids feedback
00:04:33.620 gmail.com can't wait to hear from you
00:04:38.300 trim your time did you know firefighters
00:04:42.660 respond to over a million buyers in the
00:04:45.960 United States each year
00:04:48.860 and according to reports cooking is the
00:04:53.100 leading cause behind most Home Fires
00:04:57.240 catching time today's sketch of the day
00:05:01.080 goes to 40 year old ananya
00:05:04.940 hope you learned something life-saving
00:05:07.919 today until next time it's me Dr binox
00:05:11.660 zooming out
00:05:16.139 thank you
00:05:18.000 never mind
00:05:19.390 [Music]
"""


st.set_page_config(
    page_icon="⚠️",
    page_title="Emergo",
)

st.title("⚠️Emergo")
st.caption("Learn how to react in various dangerous situations")

situation = st.radio("Choose a situation", ["Earthquake", "Flood", "Landslide", "Tornado", "Terrorist Attack", "House Fire"])

