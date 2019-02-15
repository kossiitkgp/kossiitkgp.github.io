# Kharagpur Open Source Website

Welcome to the source code of the official website of KOSS!

## How does it work?

The website is generated using [Hugo](https://gohugo.io/), an amazing static site generator written in Go. The theme used is hosted at https://github.com/kossiitkgp/koss-hugo-theme.

This website has two submodules:
 - [content/blog](https://github.com/kossiitkgp/blog)
 - [content/docs](https://github.com/kossiitkgp/docs)

 The submodules contain all the content for the indexes `/blog/` and `/docs/`.

## How to update?

To update anything at `/blog/`, go to https://github.com/kossiitkgp/blog

To update anything at `/docs/`, go to https://github.com/kossiitkgp/docs

To update anything related to design, go to https://github.com/kossiitkgp/koss-hugo-theme

## How to publish changes?

GitHub pages is hosted from the `docs/` directory of the `master` branch of this repository. Run `update.sh` to update the website. Add, Commit and Push.
