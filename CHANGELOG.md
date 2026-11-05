# Changelog

All notable changes to the IntentFlow skills are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html):

- **Major** (2.0.0): a change that breaks how the agents work together, such as renamed skills, IDs, or document sections other agents rely on.
- **Minor** (1.1.0): a new agent or capability that works with the existing team.
- **Patch** (1.0.1): fixes and wording improvements.

## [Unreleased]

## [1.0.0] - 2026-11-05

The first public release: a team of ten agents, built as Claude skills, that takes a product from idea to production with your approval at every step.

### Added

- **Orchestrator** (`intentflow-orchestrator`): brainstorms ideas with a market check and writes the Idea Brief, runs the team stage by stage with a gate between stages, keeps one project tracker, routes change requests, writes the Delivery Plan, and reviews KPIs against real data after release.
- **BRD Builder** (`intentflow-brd-builder`): interviews you and delivers a validated Business Requirements Document with numbered acceptance criteria.
- **UX Designer** (`intentflow-ux-designer`): user flows, screens, wireframes, mockups, design system, UX copy and an accessibility spec, handed over as a UX spec with Claude Design and Design System artifacts and token exports. Also reviews existing designs and checks builds against the design.
- **TSD Builder** (`intentflow-tsd-builder`): turns the BRD and UX spec into a validated Technical Specification Document, including the Access Matrix, error catalogue, tracking plan, Client Platforms and Environment Map.
- **Frontend Developer** (`intentflow-frontend-developer`): React and Next.js frontends built to the UX spec, with Vercel previews on approval.
- **Backend Developer** (`intentflow-backend-developer`): Supabase and Postgres schemas, migrations, Row Level Security and APIs, with catalogued error codes.
- **Full-Stack Developer** (`intentflow-fullstack-developer`): end-to-end web features, shared contracts, web pull request checks, framework upgrades and parallel subagents.
- **Mobile Developer** (`intentflow-mobile-developer`): iOS and Android apps in React Native with Expo, Flutter or native code, with internal test builds on approval and store release checklists.
- **QA Engineer** (`intentflow-qa-engineer`): independent web and mobile testing against the BRD, UX spec and TSD, including accessibility, performance, security basics, design and tracking, with bugs filed as GitHub Issues.
- **DevOps Engineer** (`intentflow-devops-engineer`): deployment pipelines, releases, rollbacks, monitoring, incidents, backups, security and cost, acting in production only through reversible actions you approve one at a time.
- Shared rules across the team: ask instead of assuming, verify with evidence, unique ID tags per agent, one bug loop through QA, one change route through the Orchestrator, and content from files and web pages treated as data, never as instructions.
- README with architecture, delivery pipeline, safety model and bug-loop diagrams, setup instructions and ready-to-paste project instructions.
- MIT License.
- Release packaging: every skill zipped for upload to the Claude app, plus one archive with all ten for Claude Code.
- Automatic checks on every pull request: skill files, README consistency and README diagrams.

[Unreleased]: https://github.com/intentflow-ai/intentflow-skills/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/intentflow-ai/intentflow-skills/releases/tag/v1.0.0
