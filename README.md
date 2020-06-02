## Daily CPU Updater

### _Setup_
Firebase admin json key is required in root folder named "google-service.json". In src/Main.py there is an environment 
function invoked that sets up staging or production environment.
### _What does it do_
Read assets/thoughts.json or assets/thoughts-staging.json, depending on environment, and inspects if there 
is an item on current date day, if there is, pushes an item to remote database and also marks an item in 
local json file as used. Also makes a copy of an remote database in backups/ or backups-staging/   
