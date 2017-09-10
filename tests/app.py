# -*- coding: utf-8 -*-

from .context import pathpattern
from pathpattern import *

import unittest
import logging
import sys

from igraph import Graph

class TestAppSuite(unittest.TestCase):
    """Rendering test cases."""

    log = logging.getLogger( "TestAppSuite.test_app" )
    

    def test_A_GlyphSet_tgfFile(self):
        """ """
        print "\n\n\ntest_A_GlyphSet_tgfFile\n\n"

        dfp = '/Users/jeremydouglass/Documents/Programming/github/transverse-gallery/assets/gamebooks/tgf/'
        datafiles    = [ dfp + '01-01 CYOA -- Cave of Time, The.txt.tgf'
                       , dfp + '01-05 CYOA -- Cave of Time, The.txt.tgf'
                       , dfp + '01-07 CYOA -- Cave of Time, The (115).txt.tgf'
                       , dfp + '01-07v2 CYOA -- Cave of Time, The (115).txt.tgf'
                       , dfp + '01-14 CYOA -- By Balloon to the Sahara.txt.tgf'
                       , dfp + '01-16 CYOA -- Space and Beyond.txt.tgf'
                       , dfp + '01-20 CYOA -- Mystery of Chimney Rock, The.txt.tgf'
                       , dfp + '01-24 CYOA -- Your Code Name is Jonah.txt.tgf'
                       , dfp + '01-27 CYOA -- Third Planet from Altair, The.txt.tgf'
                       , dfp + '01-29 CYOA -- Deadwood City.txt.tgf'
                       , dfp + '01-31 CYOA -- Who Killed Harlowe Thrombey.txt.tgf'
                       , dfp + '01-32 CYOA -- Who Killed Harlowe Thrombey.txt.tgf'
                       , dfp + '01-33 CYOA -- Who Killed Harlowe Thrombey.txt.tgf'
                       , dfp + '01-35 CYOA -- Lost Jewels of Nabooti, The.txt.tgf'
                       , dfp + '01-37 CYOA -- Mystery of the Maya.txt.tgf'
                       , dfp + '01-39 CYOA -- Inside UFO 54-40.txt.tgf'
                       , dfp + '01-39v2 CYOA -- Inside UFO 54-40 (labeled).txt.tgf' #
                       , dfp + '01-42 CYOA -- Abominable Snowman, The. (new edition from Jeremy collection).txt.tgf'
                       , dfp + '01-42 CYOA -- Abominable Snowman, The. (old edition from Katz collection).txt.tgf'
                       , dfp + '01-42b CYOA -- Abominable Snowman, The.txt.tgf'
                       , dfp + '01-43 CYOA -- Forbidden Castle, The.txt.tgf'
                       , dfp + '01-45 CYOA -- House of Danger.txt.tgf'
                       , dfp + '01-47 CYOA -- Survival at Sea.txt.tgf'
                       , dfp + '01-48 CYOA -- Race Forever, The.txt.tgf'
                       , dfp + '01-49 CYOA -- Underground Kingdom.txt.tgf'
                       , dfp + '01-50 CYOA -- Secret of the Pyramids.txt.tgf'
                       , dfp + '01-51 CYOA -- Escape.txt.tgf'
                       , dfp + '01-52 CYOA -- Hyperspace.txt.tgf'
                       , dfp + '01-53 CYOA -- Space Patrol.txt.tgf'
                       , dfp + '01-55 CYOA -- Lost Tribe, The.txt.tgf'
                       , dfp + '01-56 CYOA -- Lost on the Amazon.txt.tgf'
                       , dfp + '01-57 CYOA -- Prisoner of the Ant People.txt.tgf'
                       , dfp + '01-58 CYOA -- Phantom Submarine, The.txt.tgf'
                       , dfp + '01-59 CYOA -- Horror of High Ridge, The.txt.tgf'
                       , dfp + '01-60 CYOA -- Mountain Survival.txt.tgf'
                       , dfp + '01-61 CYOA -- Trouble on Planet Earth.txt.tgf'
                       , dfp + '01-65 CYOA -- Vampire Express.txt.tgf'
                       , dfp + '01-65v2 CYOA -- Vampire Express (printing-error).txt.tgf'
                       , dfp + '01-65v3 CYOA -- Vampire Express (broken).txt.tgf'
                       , dfp + '03-01 CYOA -- Inca Gold.txt.tgf'
                       , dfp + '03-02 CYOA -- Knights of the Round Table.txt.tgf'
                       , dfp + '03-03 CYOA -- Exiled to Earth.txt.tgf'
                       , dfp + '03-04 CYOA -- Master of Kung Fu.txt.tgf'
                       , dfp + '03-05 CYOA -- South Pole Sabotage.txt.tgf'
                       , dfp + '03-06 CYOA -- Mutiny in Space.txt.tgf'
                       , dfp + '03-07 CYOA -- You Are a Superstar.txt.tgf'
                       , dfp + '03-08 CYOA -- Return of the Ninja.txt.tgf'
                       , dfp + '03-09 CYOA -- Captive.txt.tgf'
                       , dfp + '03-10 CYOA -- Blood on the Handle.txt.tgf'
                       , dfp + '03-11 CYOA -- You Are a Genius.txt.tgf'
                       , dfp + '03-12 CYOA -- Stock Car Champion.txt.tgf'
                       , dfp + '03-13 CYOA -- Through the Black Hole.txt.tgf'
                       , dfp + '03-14 CYOA -- You Are a Millionaire.txt.tgf'
                       , dfp + '03-15 CYOA -- Revenge of the Russian Ghost.txt.tgf'
                       , dfp + '03-16 CYOA -- Worst Day of Your Life, The.txt.tgf'
                       , dfp + '03-17 CYOA -- Alien, Go Home.txt.tgf'
                       , dfp + '03-18 CYOA -- Master of Tae Kwon Do.txt.tgf'
                       , dfp + '03-19 CYOA -- Grave Robbers.txt.tgf'
                       , dfp + '03-20 CYOA -- Cobra Connection.txt.tgf'
                       , dfp + '03-21 CYOA -- Treasure of the Onyx Dragon, The.txt.tgf'
                       , dfp + '03-22 CYOA -- Hijacked.txt.tgf'
                       , dfp + '03-23 CYOA -- Fight for Freedom.txt.tgf'
                       , dfp + '03-24 CYOA -- Master of Karate.txt.tgf'
                       , dfp + '03-25 CYOA -- Chinese Dragons.txt.tgf'
                       , dfp + '03-26 CYOA -- Invaders from Within.txt.tgf'
                       , dfp + '03-27 CYOA -- Smoke Jumper.txt.tgf'
                       , dfp + '03-28 CYOA -- Skateboard Champion.txt.tgf'
                       , dfp + '03-29 CYOA -- Lost Ninja, The.txt.tgf'
                       , dfp + '03-30 CYOA -- Daredevil Park.txt.tgf'
                       , dfp + '03-31 CYOA -- Island of Time.txt.tgf'
                       , dfp + '03-32 CYOA -- Kidnapped!.txt.tgf' #
                       , dfp + '03-33 CYOA -- Search for Aladdin\'s Lamp.txt.tgf' #
                       , dfp + '03-34 CYOA -- Vampire Invaders.txt.tgf'
                       , dfp + '03-35 CYOA -- Terrorist Trap.txt.tgf'
                       , dfp + '03-36 CYOA -- Ghost Train.txt.tgf'
                       , dfp + '03-37 CYOA -- Behind the Wheel.txt.tgf'
                       , dfp + '03-38 CYOA -- Magic Master.txt.tgf'
                       , dfp + '03-39 CYOA -- Silver Wings.txt.tgf'
                       , dfp + '03-40 CYOA -- Superbike.txt.tgf'
                       , dfp + '03-41 CYOA -- Outlaw Gulch.txt.tgf'
                       , dfp + '03-42 CYOA -- Master of Martial Arts.txt.tgf'
                       , dfp + '03-43 CYOA -- Showdown.txt.tgf'
                       , dfp + '03-44 CYOA -- Viking Raiders.txt.tgf'
                       , dfp + '03-45 CYOA -- Earthquake.txt.tgf'
                       , dfp + '03-46 CYOA -- You Are Microscopic.txt.tgf'
                       , dfp + '03-47 CYOA -- Surf Monkeys.txt.tgf'
                       , dfp + '03-48 CYOA -- Luckiest Day of Your Life, The.txt.tgf'
                       , dfp + '03-49 CYOA -- Forgotten Planet, The.txt.tgf'
                       , dfp + '03-50 CYOA -- Secret of the Dolphins.txt.tgf'
                       , dfp + '03-51 CYOA -- Playoff Champion.txt.tgf'
                       , dfp + '03-52 CYOA -- Roller Star.txt.tgf'
                       , dfp + '03-53 CYOA -- Scene of the Crime.txt.tgf'
                       , dfp + '03-54 CYOA -- Dinosaur Island.txt.tgf'
                       , dfp + '03-55 CYOA -- Motocross Mania.txt.tgf'
                       , dfp + '03-56 CYOA -- Horror House.txt.tgf'
                       , dfp + '03-57 CYOA -- Secret of Mystery Hill, The.txt.tgf'
                       , dfp + '03-58 CYOA -- Reality Machine, The.txt.tgf'
                       , dfp + '03-59--Project UFO.txt.tgf'
                       , dfp + '03-60--Comet Crash.txt.tgf'
                       , dfp + '03-61--Everest Adventure.txt.tgf'
                       , dfp + '03-62--Soccer Star.txt.tgf'
                       , dfp + '03-63--The Antimatter Universe.txt.tgf'
                       , dfp + '03-64--Master of Judo.txt.tgf'
                       , dfp + '04-01 CYOA -- Search the Amazon.txt.tgf'
                       , dfp + '04-02 CYOA -- Who Are You.txt.tgf'
                       , dfp + '04-03 CYOA -- Gunfire at Gettysburg.txt.tgf'
                       , dfp + '04-04 CYOA -- War with the Mutant Spider Ants.txt.tgf'
                       , dfp + '04-05 CYOA -- Last Run.txt.tgf'
                       , dfp + '04-06 CYOA -- Cyberspace Warrior.txt.tgf'
                       , dfp + '04-07 CYOA -- Ninja Cyborg.txt.tgf'
                       , dfp + '04-08 CYOA -- You Are an Alien.txt.tgf'
                       , dfp + '04-09 CYOA -- U.N. Adventure.txt.tgf'
                       , dfp + '04-10 CYOA -- Sky Jam.txt.tgf' # multi-word edge label - also, remove node 0? ##
                       , dfp + '04-11 CYOA -- Tattoo of Death.txt.tgf'
                       , dfp + '04-12 CYOA -- Possessed.txt.tgf'
                       , dfp + '04-13 CYOA -- Typhoon.txt.tgf'
                       , dfp + '04-14 CYOA -- Shadow of the Swastika.txt.tgf'
                       , dfp + '04-15 CYOA -- Fright Night.txt.tgf'
                       , dfp + '05-01 CYOA-YR -- Circus, The.txt.tgf'
                       , dfp + '05-04 CYOA-YR -- Haunted House, The.txt.tgf'
                       , dfp + '05-07 CYOA-YR -- Sunken Treasure.txt.tgf'
                       , dfp + '05-10 CYOA-YR -- Your Very Own Robot.txt.tgf'
                       , dfp + '05-13 CYOA-YR -- Gorga, The Space Monster.txt.tgf'
                       , dfp + '05-14 CYOA-YR -- Search for Champ, The.txt.tgf'
                       , dfp + '05-17 CYOA-YR -- Green Slime, The.txt.tgf'
                       , dfp + '05-20 CYOA-YR -- Help You\'re Shrinking.txt.tgf' #
                       , dfp + '05-21 CYOA-YR -- Indian Trail.txt.tgf'
                       , dfp + '05-22 CYOA-YR -- Dream Trips (Go to any Page Version).txt.tgf'
                       , dfp + '05-22 CYOA-YR -- Dream Trips.txt.tgf'
                       , dfp + '05-24 CYOA-YR -- Genie in the Bottle, The.txt.tgf'
                       , dfp + '05-25 CYOA-YR -- Bigfoot Mystery, The.txt.tgf'
                       , dfp + '05-27 CYOA-YR -- Creature from Miller\'s Pond, The.txt.tgf' #
                       , dfp + '05-28 CYOA-YR -- Jungle Safari.txt.tgf'
                       , dfp + '05-29 CYOA-YR -- Mummy\'s Tomb, The.txt.tgf' #
                       , dfp + '05-30 CYOA-YR -- Three Wishes, The.txt.tgf'
                       , dfp + '05-32 CYOA-YR -- Dragons.txt.tgf'
                       , dfp + '05-33 CYOA-YR -- Wild Horse Country.txt.tgf'
                       , dfp + '05-34 CYOA-YR -- Summer Camp.txt.tgf'
                       , dfp + '05-36 CYOA-YR -- Tower of London, The.txt.tgf'
                       , dfp + '05-37 CYOA-YR -- Trouble in Space.txt.tgf'
                       , dfp + '05-39 CYOA-YR -- Mona is Missing.txt.tgf'
                       , dfp + '05-40 CYOA-YR -- Evil Wizard, The.txt.tgf'
                       , dfp + '05-41 CYOA-YR -- Polar Bear Express, The.txt.tgf'
                       , dfp + '05-44 CYOA-YR -- Flying Carpet, The.txt.tgf'
                       , dfp + '05-45 CYOA-YR -- Magic Path, The.txt.tgf'
                       , dfp + '05-46 CYOA-YR -- Ice Cave.txt.tgf'
                       , dfp + '05-47 CYOA-YR -- Fire.txt.tgf'
                       , dfp + '05-49 CYOA-YR -- Fairy Kidnap, The.txt.tgf'
                       , dfp + '05-50 CYOA-YR -- Runaway Spaceship.txt.tgf'
                       , dfp + '05-51 CYOA-YR -- Lost Dog.txt.tgf'
                       , dfp + '05-52 CYOA-YR -- Blizzard a Black Swan Inn.txt.tgf'
                       , dfp + '05-53 CYOA-YR -- Haunted Harbor.txt.tgf'
                       , dfp + '05-55 CYOA-YR -- Attack of The Monster Plants.txt.tgf'
                       , dfp + '05-56 CYOA-YR -- Miss Liberty Caper, The.txt.tgf'
                       , dfp + '05-57 CYOA-YR -- Owl Tree, The.txt.tgf'
                       , dfp + '05-58 CYOA-YR -- Haunted Halloween Party.txt.tgf'
                       , dfp + '05-59 CYOA-YR -- Sand Castle.txt.tgf'
                       , dfp + '05-60 CYOA-YR -- Caravan.txt.tgf'
                       , dfp + '05-61 CYOA-YR -- Great Easter Bunny Adventure, The.txt.tgf'
                       , dfp + '05-62 CYOA-YR -- The Movie Mystery.txt.tgf'
                       , dfp + '05-63 CYOA-YR -- Light on Burro Mountain.txt.tgf'
                       , dfp + '05-64 CYOA-YR -- Home in Time for Christmas.txt.tgf'
                       , dfp + '05-65 CYOA-YR -- You See the Future.txt.tgf'
                       , dfp + '05-66 CYOA-YR -- The Great Zopper Toothpaste Treasure.txt.tgf'
                       , dfp + '05-68 CYOA-YR -- A Day With The Dinosaurs.txt.tgf'
                       , dfp + '05-69  CYOA-YR -- Spooky Thanksgiving.txt.tgf'
                       , dfp + '05-70 CYOA-YR -- You Are Invisible.txt.tgf'
                       , dfp + '05-71 CYOA-YR -- Race of the Year.txt.tgf'
                       , dfp + '05-72 CYOA-YR -- Stranded!.txt.tgf' #
                       , dfp + '05-73 CYOA-YR -- You Can Make a Difference The Story of Martin Luther King Jr..txt.tgf'
                       , dfp + '05-74 CYOA-YR -- The Enchanted Attic.txt.tgf'
                       , dfp + '05-75 CYOA-SA -- Journey to the Year 3000.txt.tgf'
                       , dfp + '05-76 CYOA-SA -- Danger Zones.txt.tgf'
                       , dfp + '05-77 CYOA-Space Hawks -- Faster Than Light.txt.tgf'
                       , dfp + '05-78 CYOA-Space Hawks -- Alien Invaders.txt.tgf'
                       , dfp + '05-79 CYOA-Space Hawks -- Space Fortress.txt.tgf'
                       , dfp + '05-80 CYOA-Space Hawks -- The Comet Masters.txt.tgf'
                       , dfp + '05-81 CYOA-Space Hawks -- The Fiber People.txt.tgf'
                       , dfp + '05-82A CYOA-Space Hawks -- The Planet Eater.txt.tgf'
                       , dfp + '05-84 CYOA-Passport -- Tour De France.txt.tgf'
                       , dfp + '05-85 CYOA-Passport -- Forgotten Days.txt.tgf'
                       , dfp + '05-86 CYOA-Passport -- On Tour.txt.tgf'
                       , dfp + '06-06 CYON 01 Night of the Werewolf.txt.tgf'
                       , dfp + '06-07 CYON 02 Beware the Snake\'s Venom.txt.tgf' #
                       , dfp + '06-8 CYON 03 Island of Doom.txt.tgf'
                       , dfp + '06-9 CYON 04 Castle of Darkness .txt.tgf'
                       , dfp + '06-10 CYON 05 Halloween Party, The.txt.tgf'
                       , dfp + '06-11 CYON 06 Risk Your Life Arcade .txt.tgf'
                       , dfp + '06-12 CYON 07 Biting for Blood .txt.tgf'
                       , dfp + '06-13 CYON 08 Bugged Out! .txt.tgf' #
                       , dfp + '06-14 CYON 09 Mummy Who Wouldn\'t Die, The.txt.tgf' #
                       , dfp + '06-15 CYON 10 It Happened at Camp Pine Tree .txt.tgf'
                       , dfp + '06-16 CYON 11 Watch Out for Room 13.txt.tgf'
                       , dfp + '06-17 CYON 15 How I Became a Freak .txt.tgf'
                       , dfp + '06-18 CYON 16 Welcome to Horror Hospital.txt.tgf'
                       , dfp + '06-19 CYON 17 Attack of the Living Mask.txt.tgf'
                       , dfp + '06-20 CYON 18 Toy Shop of Terror, The.txt.tgf'
                       , dfp + '06-22  Goosebumps 05 Night in Werewolf Woods .txt.tgf'
                       , dfp + '06-23 Goosebumps 06 Beware of the Purple Peanut Butter.txt.tgf'
                       , dfp + '06-24 Goosebumps 07 Under the Magician\'s Spell.txt.tgf' #
                       , dfp + '06-25 Goosebumps 08 Curse of the Creeping Coffin, The.txt.tgf'
                       , dfp + '06-26 Goosebumps 09 Knight in Screaming Armor, The.txt.tgf'
                       , dfp + '06-27 Goosebumps 10 Diary of a Mad Mummy .txt.tgf'
                       , dfp + '06-28 Goosebumps 11 Deep in the Jungle of Doom.txt.tgf'
                       , dfp + '06-29 Goosebumps 12 Welcome to the Wicked Wax Museum.txt.tgf'
                       , dfp + '06-30 Goosebumps 13 Scream of the Evil Genie.txt.tgf'
                       , dfp + '06-31 Goosebumps 14 Creepy Creations of Professor Shock, The.txt.tgf'
                       , dfp + '06-32 Goosebumps 15 Please Don\'t Feed the Vampire!.txt.tgf' #
                       , dfp + '06-33 Goosebumps 16 Secret Agent Grandma .txt.tgf'
                       , dfp + '06-34 Goosebumps 17 Little Comic Shop of Horrors .txt.tgf'
                       , dfp + '06-35 Goosebumps 18 Attack of the Beastly Baby-Sitter.txt.tgf'
                       , dfp + '06-36 Goosebumps 19 Escape From Camp Run-For-Your-Life.txt.tgf'
                       , dfp + '06-37 Goosebumps 20 Toy Terror- Batteries Included.txt.tgf'
                       , dfp + '06-38 Goosebumps 21 The Twisted Tale of Tiki Island .txt.tgf'
                       , dfp + '06-39 Goosebumps 22 Return to the Carnival of Horrors .txt.tgf'
                       , dfp + '06-40 Goosebumps 23 Zapped in Space .txt.tgf'
                       , dfp + '06-41 Goosebumps 24 Lost in Stinkeye Swamp .txt.tgf'
                       , dfp + '06-42 Goosebumps 25 Shop Till You Drop...Dead!.txt.tgf' #
                       , dfp + '06-43 Goosebumps 26 Alone in Snakebite Canyon .txt.tgf'
                       , dfp + '06-44 Goosebumps 27 Checkout Time at the Dead-End Hotel .txt.tgf'
                       , dfp + '06-45 Goosebumps 28 Night of a Thousand Claws.txt.tgf'
                       , dfp + '06-46 Goosebumps 29 Invaders from the Big Screen .txt.tgf'
                       , dfp + '06-47 Goosebumps 30 You\'re Plant Food! .txt.tgf' #
                       , dfp + '06-48 Goosebumps 31 The Werewolf of Twisted Tree Lodge .txt.tgf'
                      ,dfp + '06-49 Goosebumps 32 It\'s Only a Nightmare! .txt.tgf' #
                       , dfp + '06-50 Goosebumps 33 It Came from the Internet .txt.tgf'
                       , dfp + '06-51 Goosebumps 34 Elevator to Nowhere.txt.tgf'
                       , dfp + '06-52 Goosebumps 35 Hocus-Pocus Horror.txt.tgf'
                       , dfp + '06-53 Goosebumps 36 Ship of Ghouls.txt.tgf'
                       , dfp + '06-54 Goosebumps 37 Escape from Horror House .txt.tgf'
                       , dfp + '06-55 Goosebumps 38 Into the Twister of Terror .txt.tgf'
                       , dfp + '06-56 Goosebumps 39 Scary Birthday to You! .txt.tgf' #
                       , dfp + '06-57 Goosebumps 40 Zombie School .txt.tgf'
                       , dfp + '06-58 Goosebumps 41 Danger Time.txt.tgf'
                       , dfp + '06-59 Goosebumps 42 All-Day Nightmare .txt.tgf'
                       , dfp + '07-01 Goosebumps S01 Into the Jaws of Doom (238).txt.tgf'
                       , dfp + '07-09 Nightmares -- Cave of Fear (126) --annotated.txt.tgf'
                       , dfp + '07-09 Nightmares -- Cave of Fear (126) --corrected.txt.tgf'
                       , dfp + '07-09 Nightmares -- Cave of Fear (126) --labeled.txt.tgf' #
                       , dfp + '07-09 Nightmares -- Cave of Fear (126).txt.tgf'
                       , dfp + '07-10 Nightmares -- Valley of the Screaming Statues (126).txt.tgf'
                       , dfp + '07-11 Nightmares -- Castle of Horror (126).txt.tgf'
                       , dfp + '07-12 Nightmares -- Planet of Terror (126).txt.tgf'
                       , dfp + '07-13 Lifegames 01 Woman Up the Corporate Ladder (192).txt.tgf'
                       , dfp + '07-14 Lifegames 03 Starstruck (192).txt.tgf'
                       , dfp + '07-15 Lifegames 04 Woman in Power Politics (192).txt.tgf'
                       , dfp + '07-16 Lifegames 06 Matchpoint (192).txt.tgf'
                       , dfp + '07-27 Endless Quest 06 Revenge of the Rainbow Dragons (157).txt.tgf'
                       , dfp + '07-29 Endless Quest 14 Raid on Nightmare Castle (157).txt.tgf'
                       , dfp + '07-29B Endless Quest 14 Raid on Nightmare Castle (157).txt.tgf'
                       , dfp + '07-30 Endless Quest 15 Under Dragon\'s Wing (157).txt.tgf' #
                       , dfp + '07-31 Endless Quest 16 The Dragon\'s Ransom (157).txt.tgf' #
                       , dfp + '07-32 Endless Quest 17 Captive Planet (157).txt.tgf'
                       , dfp + '07-34 Endless Quest 18 Conan the Undaunted (157).txt.tgf'
                       , dfp + '07-34 Endless Quest 18 Undaunted (157), The.txt.tgf'
                       , dfp + '07-35 Endless Quest 19 Conan and the Prophey (157).txt.tgf'
                       , dfp + '07-36 Endless Quest 21 Duel of the Masters (157).txt.tgf'
                       , dfp + '07-37 Endless Quest 22 Endless Catacombs (157).txt.tgf'
                       , dfp + '07-40 Endless Quest 24 Trouble on Artule (157).txt.tgf'
                       , dfp + '07-41 Endless Quest 25 Outlaw, The (157).txt.tgf'
                       , dfp + '07-42 Endless Quest 26 Tarzan and the Well of Slaves (157).txt.tgf'
                       , dfp + '07-43 Endless Quest 27 Lair of the Lich (157).txt.tgf'
                       , dfp + '07-44 Endless Quest 28 Mystery of the Ancients (157).txt.tgf'
                       , dfp + '07-45 Endless Quest 29 Tower of Darkness (157).txt.tgf'
                       , dfp + '07-46 Endless Quest 30 Fireseed (157), The.txt.tgf'
                       , dfp + '07-47 Endless Quest 31 Tarzan and the Tower of Diamonds (157).txt.tgf'
                       , dfp + '07-48 Endless Quest 32 Prisoner of Elderwood (157).txt.tgf'
                       , dfp + '07-49 Endless Quest 33 Knight of Illusion (159).txt.tgf'
                       , dfp + '07-50 Endless Quest 34 Claw of the Dragon.txt.tgf'
                       , dfp + '07-51 Endless Quest 35 Vision of Doom (160).txt.tgf'
                       , dfp + '07-52 Endless Quest 36 Song of the Dark Druid (160).txt.tgf'
                       , dfp + '07-53 Endless Quest Dungeon of Fear .txt.tgf'
                       , dfp + '07-54 Endless Quest Castle of the Undead.txt.tgf'
                       , dfp + '07-55 Endless Quest Secret of Djinn .txt.tgf'
                       , dfp + '07-56 Endless Quest Siege of the Tower.txt.tgf'
                       , dfp + '07-57 Endless Quest A Wild Ride.txt.tgf'
                       , dfp + '07-58 Endless Quest Forest of Darkness.txt.tgf'
                       , dfp + '07-59 Endless Quest American Knights.txt.tgf'
                       , dfp + '07-60 Endless Quest Night of the Tiger.txt.tgf'
                       , dfp + '07-61 Endless Quest Galactic Challenge.txt.tgf'
                       , dfp + '07-62 Endless Quest Bigby\'s Curse.txt.tgf' #
                       , dfp + '07-63 Endless Quest 24-Hour War.txt.tgf'
                       , dfp + '08-01--The Thundercats and the Ghost Warrior.txt.tgf'
                       , dfp + '08-02--The Thundercats and the Snowmen of Hook Mountain.txt.tgf'
                       , dfp + '08-03--The Three Investigators in The Case of the Weeping Coffin.txt.tgf'
                       , dfp + '08-04 The Three Investigators -- Case of the Dancing Dinosaur, The.txt.tgf'
                       , dfp + '08-05 The Three Investigators -- Case of the House of Horrors, The.txt.tgf'
                       , dfp + '08-06 The Three Investigators -- Case of the Savage Statue, The.txt.tgf'
                       , dfp + '09-01 Time Machine -- Blade of the Guillotine.txt.tgf'
                       , dfp + '09-01v2 Time Machine -- Blade of the Guillotine (compressed).txt.tgf'
                       , dfp + '09-03 Time Machine 15 Flame of the Inquisition.txt.tgf'
                       , dfp + '09-04 Time Machine 16 Quest for the Cities of Gold.txt.tgf'
                       , dfp + '09-05 Time Machine 17 Scotland Yard Detective.txt.tgf'
                       , dfp + '09-06 Time Machine 18 Sword of Caesar.txt.tgf'
                       , dfp + '09-07 Time Machine 19 Death Mask of Pancho Villa.txt.tgf'
                       , dfp + '09-08 Time Machine 20 Bound for Australia.txt.tgf'
                       , dfp + '09-10 Time Machine 22 Last of the Dinosaurs.txt.tgf'
                       , dfp + '09-12 Time Machine 23 Quest for King Arthur.txt.tgf'
                       , dfp + '09-13 Time Machine 24 World War I Flying Ace.txt.tgf'
                       , dfp + '09-14 Time Machine Special Edition World War II Code Breaker.txt.tgf'
                       , dfp + '09-15 Time Traveler 01 Voyage With Columbus.txt.tgf'
                       , dfp + '09-16 Time Traveler 02 Legend of Hiawatha, The.txt.tgf'
                       , dfp + '09-17 Time Traveler 03 First Settlers, The.txt.tgf'
                       , dfp + '09-18 Time Traveler 04 Amazing Ben Franklin, The.txt.tgf'
                       , dfp + '09-19 Time Traveler 05 Paul Revere and the Boston Tea Party.txt.tgf'
                       , dfp + '09-20 Time Traveler 06 George Washington and the Constitution.txt.tgf'
                       , dfp + '09-21 Be An Interplanetary Spy 01 Find the Kirillian.txt.tgf'
                       , dfp + '09-23 Be An Interplanetary Spy 02 Galactic Pirate, The.txt.tgf'
                       , dfp + '09-24 Be An Interplanetary Spy 03 Robot World.txt.tgf'
                       , dfp + '09-25 Be An Interplanetary Spy 04 Space Olympics.txt.tgf'
                       , dfp + '09-26 Be An Interplanetary Spy 05 Monsters of Doorna.txt.tgf'
                       , dfp + '09-27 Be an Interplanetary Spy 06 The Star Crystal.txt.tgf'
                       , dfp + '09-28 Be an Interplanetary Spy 07 Rebel Spy.txt.tgf'
                       , dfp + '09-29 Be an Interplanetary Spy 08 Mission to Microworld.txt.tgf'
                       , dfp + '09-30 Be an Interplanetary Spy 09 Ultraheroes.txt.tgf'
                       , dfp + '09-31 Be an Interplanetary Spy 10 Planet Hunters.txt.tgf'
                       , dfp + '09-32 Be an Interplanetary Spy 11 The Red Rocket.txt.tgf'
                       , dfp + '09-33 Be an Interplanetary Spy 12 Skystalker.txt.tgf'
                       , dfp + '09-34 Which Way Books 01 The Castle of No Return.txt.tgf'
                       , dfp + '09-35 Which Way Books 02 Vampires, Spies and Alien Beings.txt.tgf'
                       , dfp + '09-37 Which Way Books 03 The Spell of the Black Raven.txt.tgf'
                       , dfp + '09-38 Which Way Books 04 Famous and Rich.txt.tgf'
                       , dfp + '09-40 Which Way Books 05 Lost In A Strange Land.txt.tgf'
                       , dfp + '09-41 Which Way Books 06 Sugarcane Island.txt.tgf'
                       , dfp + '09-42 Which Way Books 07 Curse of the Sunken Treasure.txt.tgf'
                       , dfp + '10-01 WWY 01 Forest of Twisted Dreams, The.txt.tgf' #
                       , dfp + '10-03 WWY 02 Siege of the Dragonriders, The.txt.tgf' #
                       , dfp + '10-04 WWY 03 Who Kidnapped Princess Saralinda.txt.tgf' #
                       , dfp + '10-06 WWY 04 Ghost Knights of Camelot.txt.tgf' #
                       , dfp + '10-08 WWY 05 Haunted Castle of Ravencurse, The.txt.tgf' #
                       , dfp + '10-23 Nintendo Adventures 01 Double Trouble.txt.tgf' #
                       , dfp + '10-25 Nintendo Adventures 02 Leaping Lizards.txt.tgf' #
                       , dfp + '10-52 Zork 03 Cavern of Doom, The.txt.tgf' #
                       , dfp + '10-53 Zork 04 Conquest at Quendor.txt.tgf' #
                       , dfp + '10-54 TwistaPlot 01 Time Raider, The.txt.tgf' #
                       , dfp + '10-56 TwistaPlot 03 Formula for Trouble, The.txt.tgf' #
                       , dfp + '10-60 TwistaPlot 07 Video Avenger.txt.tgf' #
                       , dfp + '10-68 TwistaPlot 15 Spellcaster--Endings.txt.tgf' #
                       , dfp + '10-68 TwistaPlot 15 Spellcaster--Illustrations.txt.tgf' #
                       , dfp + '10-68 TwistaPlot 15 Spellcaster--Theme.txt.tgf' #
                       , dfp + '10-68 TwistaPlot 15 Spellcaster.txt.tgf' #
                       , dfp + '10-72 Explorer 01 Journey to the Center of the Atom.txt.tgf' #
                       , dfp + '10-72v2 Explorer 01 Journey to the Center of the Atom (compressed).txt.tgf' #
                       , dfp + '10-73 Explorer 02 Destination Brain--compressed.txt.tgf' #
                       , dfp + '10-73 Explorer 02 Destination Brain.txt.tgf' #
                       , dfp + '10-74 Explorer 03 In Search of a Shark.txt.tgf' #
                       , dfp + '10-75 Explorer 04 Escape from Jupiter.txt.tgf' #
                       , dfp + '11-01 Star Challenge 01 Planets in Peril.txt.tgf'
                       , dfp + '11-02 Star Challenge 02 Android Invasion, The.txt.tgf'
                       , dfp + '11-03 Star Challenge 03 Cosmic Funhouse, The.txt.tgf'
                       , dfp + '11-04 Star Challenge 05 Galactic Raiders.txt.tgf'
                       , dfp + '11-05 Star Challenge 06 Weird Zone, The.txt.tgf'
                       , dfp + '11-07 Star Challenge 07 Dimension of Doom.txt.tgf'
                       , dfp + '11-08 Star Challenge 08 Lost Planet, The.txt.tgf' #
                       , dfp + '11-09 Star Challenge 09 Moons of Mystery.txt.tgf'
                       , dfp + '11-10 Star Challenge 10 Haunted Planet, The.txt.tgf'
                       , dfp + '11-11 EFT 01 Tenopia Island.txt.tgf' #
                       , dfp + '11-11v2 EFT 01 Tenopia Island (no maps).txt.tgf' #
                       , dfp + '11-11v3 EFT 01 Tenopia Island (no maps, simplified).txt.tgf' #
                       , dfp + '11-12 EFT 02 Trapped in the Sea Kingdom.txt.tgf'
                       , dfp + '11-13 EFT 03 Terror on Kabran.txt.tgf'
                       , dfp + '11-14 EFT 04 Star System Tenopia.txt.tgf'
                       , dfp + '11-15 EFKF 01 Castle of Frome, The.txt.tgf'
                       , dfp + '11-16 EFKF 02 The Forest of the King.txt.tgf'
                       , dfp + '11-17 EFKF 02 The Caverns of Mornas.txt.tgf'
                       , dfp + '11-19 EFKF 04 The Battle of Astar.txt.tgf'
                       , dfp + '11-20 YAA 01 The Castle of Doom.txt.tgf'
                       , dfp + '11-21 YAA 02 Island of Fear.txt.tgf'
                       , dfp + '11-22 YAA 03 Terror Under the Earth.txt.tgf'
                       , dfp + '11-23 YAA 04 The Dragonmaster.txt.tgf'
                       , dfp + '11-24 YAA 05 Revenge of the Dragonmaster.txt.tgf'
                       , dfp + '11-25 Scream Shop 01 Abracadanger.txt.tgf'
                       , dfp + '11-26 Scream Shop 02 Now You See Me, Now You Don\'t!.txt.tgf' #
                       , dfp + '11-27 Scream Shop 03 Eye Spy Aliens.txt.tgf'
                       , dfp + '11-28 Scream Shop 04 Revenge of the Gargoyle.txt.tgf'
                       , dfp + '13-01 PYOHS -- Craven House Horrors (116).txt.tgf'
                       , dfp + '13-09 PIYAS -- Staying Alive (152).txt.tgf'
                       , dfp + '13-10 PIYAS -- Star Trek III (117) one ending.txt.tgf'
                       , dfp + '13-11 PIYAS -- Star Trek II (126).txt.tgf'
                       , dfp + '13-12 Storytrails -- Stone of Badda.txt.tgf'
                       , dfp + '13-19 Rollercoaster Tycoon -- Sudden Turn.txt.tgf'
                       , dfp + '13-25 IYC -- Serena\'s Secret (80).txt.tgf' #
                       , dfp + '13-28 Powerpuff Girls -- Career-Day Blossom (64).txt.tgf'
                       , dfp + '13-56B Survivor -- Thailand.txt.tgf'
                       , dfp + '13-60 Troll AA -- Cosmic Kidnappers (116) remediates computer functions.txt.tgf' #
                       , dfp + '13-61 Troll AA -- Target Earth (116).txt.tgf'
                       , dfp + '13-62 Troll AA -- Town in Terror (116).txt.tgf'
                       , dfp + '13-63 Troll AA -- Thieves from Space (118).txt.tgf'
                       , dfp + '13-66 Troll FA -- Secret of the Old Museum (99) interesting middle branch.txt.tgf' #
                       , dfp + '13-67 Troll FA -- Mystery at Loch Ness (99).txt.tgf'
                       , dfp + '13-70 Troll FF -- War of the Wizards.txt.tgf'
                       , dfp + '13-71 Troll FF -- Master of Mazes.txt.tgf'
                       , dfp + '13-72 Troll FF -- Magician\'s Ring.txt.tgf'
                       , dfp + '13-73 ** Troll FF -- Forbidden Towers (124).txt.tgf'
                       , dfp + '13-74 Troll SIY -- Mystery at the Bike Race (122).txt.tgf'
                       , dfp + '13-76 Troll SIY -- Missing Rock Star Caper (117).txt.tgf'
                       , dfp + '14-01 What If Books 01 Ride the Blue Bazoo.txt.tgf'
                       , dfp + '14-02 What If Books 02 Follow the Lone Cry.txt.tgf'
                       , dfp + '14-03 What If Books 03 Sneek Behind Enemy Lines.txt.tgf'
                       , dfp + '14-04 What If Books 04 Accept the Royal Challenge.txt.tgf'
                       , dfp + '14-05 Turning Points 01 Friends Forever.txt.tgf'
                       , dfp + '14-06 Turning Points 02 Kerry\'s Dance.txt.tgf' #
                       , dfp + '14-07 Turning Points 03 Valentine for Betsy.txt.tgf'
                       , dfp + '14-08 Turning Points 04 Forget Me Not.txt.tgf'
                       , dfp + '14-09 Turning Points 05 Keep Tomorrow for Me.txt.tgf'
                       , dfp + '14-10 Follow Your Heart Romance 01 Summer in the Sun.txt.tgf'
                       , dfp + '14-11 Follow Your Heart Romance 04 Sun, Sea and Boys.txt.tgf'
                       , dfp + '14-12 Follow Your Heart Romance 08 Lots of Boys.txt.tgf'
                       , dfp + '14-13 Follow Your Heart Romance 10 Seven Boy Vacation.txt.tgf'
                       , dfp + '14-14 Dream Your Own Romance 02 Holiday Romance.txt.tgf'
                       , dfp + '14-15 Make Your Dreams Come True -- Angie\'s Choice.txt.tgf' #
                       , dfp + '14-15 Make Your Dreams Come True 01 Angie\'s Choice.txt.tgf' #
                       , dfp + '14-16 Make Your Dreams Come True 02 Winning at Love.txt.tgf'
                       , dfp + '14-17 Make Your Dreams Come True -- Worthy Opponents.txt.tgf'
                       , dfp + '14-18 Make Your Dreams Come True -- Dream Date.txt.tgf'
                       , dfp + '14-21 Pick Your Own Dream Date -- Saturday Night Bash, The.txt.tgf'
                       , dfp + '14-22 Pick Your Own Dream Date -- Spring Break.txt.tgf'
                       , dfp + '14-23 Confidentially Yours -- Confidentially Yours.txt.tgf'
                       , dfp + '14-24 Confidentially Yours -- Breaking Up is Hard to Do.txt.tgf'
                       , dfp + '14-25 Date with Destiny Adventures -- Escape From Fire Island.txt.tgf'
                       , dfp + '14-26 Date with Destiny Adventures -- Night of a Thousand Boyfriends.txt.tgf'
                       , dfp + '14-27 Find Your Fate - Jem 01 Jewels in the Dark.txt.tgf'
                       , dfp + '14-28 Find Your Fate - Jem -- Video Caper, The.txt.tgf'
                       , dfp + '14-29 Find Your Fate - Jem -- Secret of Rainbow Island.txt.tgf'
                       , dfp + '14-32 Ghostwriter -- Match of Wills.txt.tgf'
                       , dfp + '14-33 Ghostwriter -- Amazement Park Adventure.txt.tgf'
                       , dfp + '14-34 Sexuality Decision- Making Series -- Taking Chance with Sex.txt.tgf'
                       , dfp + '14-38 Thrilling Adventures in Space -- Space Pilot.txt.tgf'
                       , dfp + '14-40 Have Your Own Extra-Terrestrial Adventure.txt.tgf'
                       , dfp + '14-41 You Can Be -- The Stainless Steel Rat.txt.tgf'
                       , dfp + '14-43 Make Your Own Adventure With -- Doctor Who, The Garden of Evil.txt.tgf'
                       , dfp + '14-44 Micro Adventure -- Robot Race.txt.tgf'
                       , dfp + '14-45 Star Challenge -- The Exploding Suns.txt.tgf'
                       , dfp + '14-48 Find Your (Unfortunate) Fate --Tales from the Crypt-Name Your Nightmare.txt.tgf'
                       , dfp + '14-49 Animorphs Alternamorphs -- Next Passage, The.txt.tgf'
                       , dfp + '14-50 Animorphs Alternamorphs -- First Journey.txt.tgf'
                       , dfp + '14-51 Paths of Doom -- Sete-Ka\'s Dream Quest.txt.tgf' #
                       , dfp + '14-54 Make It Happen -- Master of the Past.txt.tgf'
                       , dfp + '14-58 Tracker Books -- Codebreaker.txt.tgf'
                       , dfp + '14-59 Tracker Books -- Skyjacked.txt.tgf'
                       , dfp + '14-63 Storymaze -- The Golden Udder.txt.tgf'
                       , dfp + '14-65 Storymaze -- Minaotaur\'s Maze, The.txt.tgf' #
                       , dfp + '14-66 You Are There -- Battle of the Alamo.txt.tgf'
                       ]

        tests = zip(datafiles)

        for t in tests:

            ## SETUP GRAPH
            print t
            tf = tgfFile(t[0])
            tfg = tf.to_graph()

            ## CREATE GLYPHSET
            gs = GlyphSet(graph=tfg, outdir='../output/pyx_glyphs/', prefix=filelabel(t[0]))
            print '  id:  ' + gs.id
            print gs
            # print gs.gcounts

            ## WRITE SIGNATURE IMAGE W/COUNT COLORS
            gs.write_signature()
            
            ## WIPE COUNT COLORS AND WRITE GLYPH IMAGES
            ## We could recreate the gs Glyphset with new settings -- but not necessary.
            gs.nocounts()      # set all counts to 1
            # gs.write_glyphs()  # write the glyph images
            ## Update the file prefix to avoid overwriting the first sig
            gs.prefix = gs.prefix + 'nocounts_'
            gs.write_signature()

            # print tf
            # print gsl
            # print gs
            # print 'len(tf):  ' + str(len(tf) )
            # # print 'len(tfg): ' + str(len(tfg))
            # print 'len(gsl): ' + str(len(gsl))
            # print 'len(gs): ' + str(len(gs))
            
            # self.assertEqual( len(tf), len(tfg))
            # self.assertEqual( len(gsl), len(gs))
            # self.assertEqual( len(gs), len(tf))
            # self.assertEqual( len(gs), len(tfg))
            # self.assertEqual( len(gsl), len(tf))
            # self.assertEqual( len(gsl), len(tfg))

    @unittest.skip("skipping: currently batch testing _A_ sigs only")
    def test_AA_GlyphSet_tgfFile_batch(self):
        """ Collect a set of graphs into one huge metagraph """
        print "\n\n\ntest_A_GlyphSet_tgfFile_batch\n\n"

        datafiles    = [ '../input/tgf/Lies_(Rick_Pryll).tgf'
                       , '../input/tgf/love is not CYOA.txt.tgf'
                       , '../input/tgf/Paper_Pong.tgf'                      # core.py 177: IndexError: list index out of range 
                       , '../input/tgf/Queneau_a-story-as-you-like-it.tgf'
                       , '../input/tgf/Sheldon_cookie.tgf'                  # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/Thrusts of Justice.tgf'              # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/TutorText0.tgf'
                       , '../input/tgf/jsayers.tgf'
                       , '../super_mario_bros/super_mario_bros-levels.tgf'
                       , '../input/tgf/Yorick.txt.tgf'
                       , '../input/tgf/CYOA_018.tgf'
                       , '../input/tgf/CYOA_112.tgf'
                       , '../input/tgf/Hopscotch_combined.tgf'
                       , '../input/tgf/Hopscotch_TOC1.tgf'
                       , '../input/tgf/Hopscotch_TOC2.tgf'
                       ]

        tests = zip(datafiles)

        metagraph = Graph(directed=True)

        for t in tests:
            ## SETUP GRAPH
            # print t
            tf = tgfFile(t[0])
            tfg = tf.to_graph()
            metagraph = metagraph.disjoint_union(tfg)
            ## each graph is added to the main graph, then the combined will be rendered as normal
            ## http://stackoverflow.com/questions/12058917/simple-python-igraph-usage
            ## http://igraph.org/python/doc/igraph.GraphBase-class.html#disjoint_union
            
        ## CREATE GLYPHSET
        gs = GlyphSet(graph=metagraph, outdir='../output/pyx_glyphs/', prefix=filelabel('metagraph'))
        print '  id:  ' + gs.id
        print gs
        # print gs.gcounts

        gs.write_signature()  # write sig image w/ counts
        gs.nocounts()         # set all counts to 1
        gs.write_glyphs()     # write glyph images w/ no counts
        gs.prefix = 'metagraph_nocounts_'
        gs.write_signature()  # write sig image w/ counts


    @unittest.skip("skipping: currently batch testing _A_ sigs only")
    def test_AAA_GlyphSet_tgfFile_diff(self):
        """ Calculate the difference between GlyphSets """
        print "\n\n\ntest_A_GlyphSet_tgfFile_batch\n\n"

        datafiles0   = [ '../input/tgf/CYOA_018.tgf' 
                       , '../input/tgf/Hopscotch_TOC1.tgf'
                       ]

        datafiles1   = [ '../input/tgf/CYOA_112.tgf'      
                       , '../input/tgf/Hopscotch_TOC2.tgf'
                       ]

        tests = zip(datafiles0,datafiles1)

        for t in tests:
            tf0 = tgfFile(t[0])
            tfg0 = tf0.to_graph()
            gs0 = GlyphSet(graph=tfg0, outdir='../output/pyx_glyphs/', prefix=filelabel(t[0]))
            gs0.write_signature()
            
            tf1 = tgfFile(t[1])
            tfg1 = tf1.to_graph()
            gs1 = GlyphSet(graph=tfg1, outdir='../output/pyx_glyphs/', prefix=filelabel(t[1]))
            gs1.write_signature() 
            

            ## our comparisons will be thrown off if glyphs have count numbers, so wipe them first
            gs0.nocounts()         # set all counts to 1
            gs1.nocounts()         # set all counts to 1

            ## if we were adding the lists, we would use +:
            ##   gsL = gs0.glist+gs1.glist
            ## ...but we are getting the difference:
            ## http://stackoverflow.com/questions/3462143/get-difference-between-two-lists
            ## e.g. list(set(liA) - set(liB))
            gsL = list(set(gs0.glist) - set(gs1.glist))
            gs = GlyphSet(list=gsL, outdir='../output/pyx_glyphs/', prefix=filelabel(t[0])+filelabel(t[1]))

            ## currently combining initialized lists in a new object messes up counts and throws an error, as the counts are preserved from their individual lists...?
            ##   e.g.  if r<0 or r>1 or g<0 or g>1 or b<0 or b>1: raise ValueError            
            ## ...counts were already stripped above, but just for good measure in case that changes,
            ## ...I'll just strip counts for now
            gs.nocounts()         # set all counts to 1
            gs.write_glyphs()     # write glyph images w/ no counts
            gs.write_signature()  # write sig image w/ counts

    @unittest.skip("skipping: currently batch testing _A_ sigs only")
    def test_B_tgfFile(self):
        """ """
        print "\n\n\ntest_B_tgfFile\n\n"
        datafiles    = [ 
                         '../input/tgf/Lies_(Rick_Pryll).tgf'
                       , '../input/tgf/love is not CYOA.txt.tgf'
                       , '../input/tgf/Paper_Pong.tgf'                    # core.py line 177: IndexError: list index out of range
                       , '../input/tgf/Queneau_a-story-as-you-like-it.tgf'
                       , '../input/tgf/Sheldon_cookie.tgf'                # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/Thrusts of Justice.tgf'            # core.py 172: ValueError: dictionary update sequence element #0 has length 0; 2 is required
                       , '../input/tgf/TutorText0.tgf'
                       , '../input/tgf/jsayers.tgf'
                       , '../super_mario_bros/super_mario_bros-levels.tgf'
                       , '../input/tgf/Yorick.txt.tgf'
                       , '../input/tgf/CYOA_018.tgf'
                       , '../input/tgf/CYOA_112.tgf'
                       , '../input/tgf/Hopscotch_combined.tgf'
                       , '../input/tgf/Hopscotch_TOC1.tgf'
                       , '../input/tgf/Hopscotch_TOC2.tgf'
                       ]
        edgecounts   = [ 82,
                         184,
                         336,
                         38,
                         22,
                         202,
                         40,
                         42,
                         42,
                         22,
                         108,
                         92,
                         209,
                         55,
                         154
                       ]
        tests = zip(datafiles, edgecounts)
        
        for t in tests:
            print t
            tf = tgfFile(t[0])
            self.assertTrue(tf.nodelist)
            self.assertTrue(tf.nodeset)
            self.assertTrue(tf.nodedict)
            self.assertTrue(tf.edgelist)
            self.assertTrue(tf.filename)
            # print tf
            self.assertEqual(len(tf),t[1])
            ef = tf.write_edgefile()
            print '  saving:  ' + str(ef) + '\n'

    @unittest.skip("skipping: currently batch testing _A_ sigs only")
    def test_C_GlyphSet_ranges(self):
        """ """
        print "\n\n\ntest_C_GlyphSet_ranges\n\n"
        ranges       = [ ((1,3),(2,4)),
                         ((0,2),(1,2)),
                         ((0,4,'indegree',1),(0,4,'outdegree',1)), # label and 'counts' args ignored for ranges
                         ((0,4),(0,4)),
                         ((0,5),(0,5))
                       ]
        expect_len   = [  4,
                          2,
                         16,
                         16,
                         25
                       ]
        tests = zip(ranges,expect_len)

        for t in tests:
            print t 
            gs = GlyphSet(range=t[0], outdir='../output/pyx_glyphs/', prefix='test_GS_range_')
            print gs.id
            print gs
            # self.log.debug( 'len: ' + str(len(gs)) + ' : ' + str(t[1]))
            self.assertEqual( len(gs), t[1])
            gs.write_glyphs()
            gs.write_signature()
            # print gs.gcounts
            print '\n'

    @unittest.skip("skipping: currently batch testing _A_ sigs only")
    def test_D_GlyphSet_lists(self):
        """ """
        print "\n\n\ntest_D_GlyphSet_lists\n\n"

        lists        = [ [(0,1),(1,0),(1,1),(1,2)]
                       , [(0,1),(1,0),(1,1),(1,2),(2,1),(1,3)]
                       , [(0,0),(0,1),(1,0),(1,1),(1,2),(1,3),(2,1),(2,2)]
                       , [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
                       , [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
                       #, [(0,1,20),(1,0,99),(1,1,50),(1,2,17)] # counts? will fail because degree_glyph isn't dynamically setting the range
                       , [(0,1,1),(1,0,2),(1,1,3),(1,2,2)]
                       ]
        expect_len   = [ 4
                       , 6
                       , 8
                       , 9
					   , 16
                       , 4
                       ]
        
        tests = zip(lists,expect_len)

        for t in tests:
            print t
            gs = GlyphSet(list=t[0], outdir='../output/pyx_glyphs/', prefix='test_GS_list_')
            print gs.id
            print gs
            # self.log.debug( 'len: ' + str(len(gs)) + ' : ' + str(t[1]))
            self.assertEqual( len(gs), t[1])
            gs.write_glyphs()
            gs.write_signature()
            # print gs.gcounts
            print '\n'

    @unittest.skip("skipping: currently batch testing _A_ sigs only")
    def test_E_pp_graph_stats(self):

        def tprint(*args):
            for a in args:
                print a

        g = Graph(directed=True)
        g.add_vertices(11)
        g.add_edges([(0,1), (1,2), (1,3), (2,4), (2,5), (3,5), (3,6), (4,7), (4,8), (5,8), (5,9), (6,9), (6,10)])

        a, b = pp_graph_stats(g)

        print 'parse arguments:'
        tprint(1,2,3)
        tprint(a)
        tprint(b)
        tprint(a[0])
        tprint(*a)
        tprint(*a[0])
        tprint(*a[0][0])



    @unittest.skip("skipping: currently batch testing _A_ sigs only")
    def test_twineFile(self):
        """ """
        print "\n\n\ntest_twineFile\n\n"

        datafiles    = [ '../input/twine/twine_archive.html'
                       , '../input/twine/howlingdogs.html'
                       , '../input/twine/The_Temple_of_No.html'
                       ]

        formats      = [ 'archive'
                       , 'published'
                       , 'published'
                       ]

        tests = zip(datafiles, formats)

        for t in tests:
            print t
            tf = twineFile(t[0], format=t[1])
            print tf
            len(tf)
            tfg = tf.to_graph()
            gs = GlyphSet(graph=tfg, outdir='../output/pyx_glyphs/', prefix=filelabel(t[0]))
            print '\n'
            gs.write_glyphs()
            gs.write_signature()



























        

#    def test_app(self):
#        outpath = '../output/pyx_glyphs/'
#
#        log = logging.getLogger( "TestAppSuite.test_app" )
#        log.debug( "test_app" )
#
#        log.debug( "0a. glyph set" )
#        gs = GlyphSet( list = [(0,0),(0,1),(1,1),(1,2),(2,1),(1,3),(1,0)], width=2 )
#        gs = GlyphSet( range = ((0,4),(0,4)) )
#        print len(gs) # count of glyphs
#        print gs      # print glyph tuples by width
#        gs.write_glyph((0,1))
#        gs.write_glyphs()
#        
#        log.debug( "0b. signature template" )
#        signature_template = gs.signature()
#        signature_template.writeGSfile(filename= outpath + 'signature_template.png')
#        signature_template.writeGSfile(filename= outpath + 'signature_template.jpg')
#
#        log.debug( "1. work: import data")
#        tgffile_to_edgelist('../super_mario_bros/super_mario_bros-levels.tgf','../super_mario_bros/super_mario_bros-levels.el')
#        smb_graph = edgelistfile_to_graph('../super_mario_bros/super_mario_bros-levels.el')
#        print smb_graph
#
#        log.debug( "2. work: stats")
#        smb_stats = pp_graph_stats(smb_graph)
#        print smb_stats # custom print http://stackoverflow.com/questions/1535327/how-to-print-a-class-or-objects-of-class-using-print
#        
#        log.debug( "3. work: signature")
#        smb_signature = signature(smb_graph)
#        print smb_signature
#        smb_signature.writeGSfile(filename= outpath + 'smb_signature.jpg')
#        # smb_sig.dump('../super_mario_bros/super_mario_bros-levels.sig.png')
#
#        log.debug( "4. work: find motif")
#        #
#
#        log.debug( "5. corpus: import data")
#        # corpus_graph_set = tgfdir_to_graph_set('')
#
#        log.debug( "6. corpus: stats")
#        # corpus_stats = pp_stats_set(corpus_graph_set)
#
#        log.debug( "7. corpus: signature")
#        #
#
#        log.debug( "8. corpus: find motif")
#        
#        
#        log.debug( "9. work / corpus: comparison stats")
#        #
#
#        log.debug( "10. work / corpus: comparison signature")
#        #
#
#        log.debug( "11. work / corpus: comparison motif")
#        #

if __name__ == '__main__':
    # create logger
    # logging.basicConfig( stream=sys.stderr )
    # logging.basicConfig( stream=sys.stderr, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' )
    logging.basicConfig( stream=sys.stderr, format='--------------------\n%(asctime)s - %(name)s - %(levelname)s\n%(message)s\n' )

    logging.getLogger( "TestAppSuite.test_app" ).setLevel( logging.DEBUG )

    unittest.main()

    