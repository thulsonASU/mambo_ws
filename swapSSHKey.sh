#!/bin/bash
ssh-add -D
ssh-add ~/.ssh/id_mambo

# verify connection
ssh -T git@github.com
