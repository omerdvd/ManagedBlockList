# Contributing to DNS Allow and Block Lists

First off, thank you for considering contributing! Community-driven lists stay relevant through collective effort, and your input helps make this resource better for everyone.

By participating in this project, you agree to abide by the terms outlined below.

---

## Our Philosophy

The goal of this repository is to provide reliable, high-quality DNS filtering lists. To maintain the integrity and performance of these lists, we prioritize **accuracy** over **quantity**.

## How Can I Contribute?

### Suggesting New Entries
If you have a domain that should be blocked (malware, tracking, etc.) or a legitimate domain that is currently being "false-positively" blocked, please open an **Issue**.

* **Check for duplicates:** Search existing issues and pull requests to see if the domain has already been discussed.
* **Provide Evidence:** When suggesting a block, include a brief reason or evidence (e.g., a link to a malware scan or a description of the tracker).
* **One Topic per Issue:** Please do not bundle unrelated domains into a single request.

### Submitting Pull Requests
If you prefer to submit changes directly via a Pull Request (PR):

1.  **Fork the repository** and create your branch from `main`.
2.  **Format consistently:** Ensure your additions follow the existing syntax of the list (e.g., `@@||domain.com^` and `||domain^`).
3.  **Alphabetical Order:** If the list is alphabetized, please place your entry in the correct spot.
4.  **Describe the change:** Clearly state what was added or removed and why.

---

## Decision Process and Final Authority

To ensure the stability of these lists for all users, the following rules apply to all contributions:

* **Final Word:** As the project maintainer, I reserve the right to accept or reject any contribution (Issue or Pull Request) at my sole discretion. 
* **Subjective Criteria:** A domain may be rejected if it doesn't align with the project’s goals, even if it technically meets the criteria for a blocklist.
* **No Obligation:** Submission of a PR does not guarantee it will be merged. I may close PRs without merging if I feel the change is not a fit for the "official" version of this list.
* **Reversals:** I reserve the right to remove any previously accepted entries at any time if they are found to cause issues or no longer meet project standards.

## Code of Conduct

Be respectful and concise in your communication. We are all here to build a better web experience.

---

## Questions?

If you are unsure whether a contribution is appropriate, feel free to open an Issue with the tag `question` before doing the work.
