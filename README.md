# Heroku BoomPow Client

Deploy BANANO's super official Proof of Work system (BoomPoW) on Heroku to earn free BAN.

## Requirements

1. A free [Heroku account](https://signup.heroku.com/signup/dc).

## Prepare the app

Clone this repository so that you have a local version of the code that you can then deploy to Heroku, execute the following commands in your local command shell or terminal:

```shell
git clone https://github.com/jacektrocinski/heroku-banano-boompow.git
cd heroku-banano-boompow
```

## Deploy the app

Before continuing, make sure [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) is installed.

```shell
heroku apps:create banano-boompow
heroku buildpacks:add heroku/python --app banano-boompow
heroku buildpacks:add --index 1 heroku-community/apt --app banano-boompow
```

Replace `YOUR_BANANO_ADDRESS` in `start.sh` with your BAN address and commit the change.

Deploy the app.

```shell
git push heroku main
heroku ps:scale worker=1 --app banano-boompow
```

## Useful commands

View recent logs.

```shell
heroku logs --app banano-boompow
```

Deploy from a branch besides `main`.

```shell
git push heroku dev:main
```

## Receiving upstream commits

The git remote for `bpow-main` should be https://github.com/BananoCoin/boompow/tree/master/client

Get the latest changes to BoomPoW:

```
git checkout bpow-main
git pull
```

Next, update `bpow-client` with the new filtered version of the commits.

```shell
git subtree split --client/ --onto bpow-client -b bpow-client
```

With `bpow-client` now updated, you can update the `main` branch as you see fit (either by merging or rebasing).

```shell
git checkout main
git rebase bpow-client
```

- `main` - Main branch.
- `dev` - Development branch.
-

Sources

1. https://stackoverflow.com/questions/24577084/forking-a-sub-directory-of-a-repository-on-github-and-making-it-part-of-my-own-r
1. https://github.com/zh/banano-awesome/blob/master/assets/How-to-setup-bPoW-on-Heroku.md
