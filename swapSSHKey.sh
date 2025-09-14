eval `ssh-agent -s` # start the agent first ******** <- curse word
ssh-add -D
ssh-add ~/.ssh/id_mambo

# verify connection
ssh -T git@github.com
