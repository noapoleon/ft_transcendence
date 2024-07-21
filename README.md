# ft_transcendence
Last 42 common core project

Clean 
```sh
sudo apt-get clean
sudo apt-get autoremove
sudo apt-get purge $(dpkg -l | awk '/^rc/ { print $2 }')
sudo rm -rf /var/cache/*
sudo journalctl --vacuum-time=1d
rm -rf ~/.local/share/Trash/*
```

# Changelog
Put here changes that will impact project mates
### 2024-07-01
- moved all sources from `srcs/requirements` to `services`
- added a few makefile rule aliases like `make down` which is the same as `make stop`
- removed all `--no-print-directory` in favor of a `MAKEFLAGS` approach

# FAQ
### Why specific version of docker image instead of `latest`?
- Prevents random non functioning project in the future, for example, during the evaluation if image has changed

# TODO
### Stuff for later
- [ ] music error message when doing nothing `Autoplay was prevented: DOMException: play() failed because the user didn't interact with the document first. https://goo.gl/xX8pDD` `music.js:14`
- [ ] logout button not working because of music button
    - TODO: remove temporary logout button from `templates/navbar.html`, and uncomment music.js but first fix the constant loop trying to play it
- [ ] does forfeiting a game mark it as over?
- [ ] join button not working? no error in chrome console
- [ ] nginx 10s to close (not critical but worth investigating)
### Stuff to fix (my work)
- [x] refreshing multi config page gives `Page not found (404)`
    - FIX: forgot to add `/multi` to urls path, not sure why it was working at all, probably because page is static
- [x] play button in multi config redirecting to normal game
- [ ] when refreshing host particles stay on guest
- [ ] sometimes there's an AI in multi game, not sure how to recreate
### Multiplayer
- Stuff to create:
    - dont know where yet:
        - [x] update score remotely
        - [x] countdown
        - [x] trigger `player` wins this game! text
        - [ ] reloading finished game:
            - [ ] Problem 1: if host reloads his finished game it will be an AI background game but guest will stream that game
            - [ ] Problem 2: countdown plays for some reason
        - [ ] rotate game field 180 degrees and invert inputs if `isMultiNotHost()` (later to`isMultiGuest()`) (dont invert colors)
            - [ ] need to interpolate too
        - [ ] redirect home if not allowed to see a game
        - [x] game creation select player with searchPlayer in stateMachine (started making template already), need to change buttons behavior
        - [ ] create template/view for pausing game when one of the two players is not connecte
        - [x] when p2 is handled remove public access to games, no more spectators (in `views.py`), `isSpectator()`
        - [ ] resume game in terrain center and start timer
        - [ ] disable `save()` function on games that are finished just in case
        - [ ] add a `Waiting for {{p2.name}}...` on same field as countdown when user is not here
        - [ ] fix small field size when nothing inside
        - [ ] why is notif also sent to game host? actually this might not be a bad thing 
    - in `views.py`: (not right file name)
        - [x] `multiConfig()`
        - [x] added `gameType` to `getGame()`
        - [ ] for multiplayer, only host should be allowed to save game
    - in `urls.py`:
    - in `StateMachine.js`:
        - [ ] in Multiplayer config use `Name` field and custom search, no fancy list of matching names, shake red (like wrong password in login form, if player doesn't exist
    - in `templates`:
        - [x] `website/multiConfig.html`
            - [ ] add opponent selector like in tournament creator
    - in `consumer.py`:
        - [ ] receive method seems to do everything, no if checks for type, ask guillaume
        - [x] receive data in a smarter way for hostGameInfo only using a `type` field as a proof of concept
    - in `Pong.js`:
        - [ ] ask guillaume why `gameType` is not reset in `resetGameInfo()` and `toState()`
            - I believe its causing some issues at the end of games
        - [x] variable that holds multi game info/data, `multiData`
            - These functions should set `multiData` properly if needed
                - [ ] `initGameVariable()`
                - [ ] `resetGameInfo()`
                - [ ] `toState()`
                - [ ] `preConfig()`
                - [ ] `postConfig()`

    - in multi config page:
        - [ ] keep normal dumb player list for now
        - [ ] after searching for a player if clicked make input field become button like player 1 above, except you can hover and click it to remove, becomes search field again
        - [ ] add `id=delPlayer` button somewhere
        - [ ] after choosing 
