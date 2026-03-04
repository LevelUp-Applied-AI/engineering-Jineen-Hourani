# PR Self-Review Checklist

Before opening a pull request, I verify the following:

- [ ] The code does what the PR title and description claim (correctness)
- [ ] All tests pass locally and no existing functionality is broken
- [ ] There are tests covering the new or modified behavior (if applicable)
- [ ] The scope of this PR is focused on one logical change
- [ ] There are no debug artifacts (e.g., print statements, breakpoint(), temp files)
- [ ] The README or documentation is updated if behavior changed
- [ ] Commit messages are clear and meaningful