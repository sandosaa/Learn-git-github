# Git Pro-Tips & Cool Tricks

some tricks i use to in my day time to time as i'm not using zsh aliases anyway

## 1. Interactive Staging (`git add -p`)

Instead of staging an entire file, stage individual "hunks" of code. This allows you to create clean, focused commits even if you've worked on multiple features at once.

```bash
git add -p
```

## 2. Fixup the Last Commit (`git commit --amend`)

Forgot a semicolon or a small detail? Don't create a "fix" commit. Merge it into the previous one.

```bash
git add .
git commit --amend --no-edit
```

## 3. The Time Machine (`git reflog`)

Ever deleted a branch or performed a hard reset and thought you lost work? Git keeps a log of every movement of `HEAD` unless it's garbage collected.

```bash
git reflog
# Find the SHA of the state you want to return to
git reset --hard <SHA>
```

## 4. Visualizing History (`git log --graph`)

Make the log readable and see how branches diverge and merge.

```bash
git log --oneline --graph --decorate --all
```

## 5. Binary Search for Bugs (`git bisect`)

Automate finding the exact commit that introduced a bug.

```bash
git bisect start
git bisect bad                 # Current version is broken
git bisect good <commit-hash>  # This old version worked
# Git will check out a middle commit. Tell it if it's 'good' or 'bad'.
```

## 6. Personal Aliases

Stop typing long commands. Add these to your `~/.gitconfig`:

```ini
[alias]
  st = status
  co = checkout
  br = branch
  lg = log --oneline --graph --all
```

## 7. Stash Specific Files

You don't have to stash everything.

```bash
git stash push -m "work in progress" path/to/file.txt
```
