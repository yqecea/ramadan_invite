## 🎯 ДЛЯ ТЕБЯ (Простым языком)
### Что будет сделано?
- Мы создадим новую, минималистичную версию пригласительного (назовем проект `ramadan-ahi`, чтобы оно не мешало первой версии).
- В дизайне будут использованы строгие цвета (черный, белый, оттенки серого), акцентная типографика (Aura-style) и геометрические узоры из референса.
- Мы поменяли дату с 14 числа на 15, как ты и просил.
- Сохраним все полезные функции: таймер, карту, кнопку «Добавить в календарь», но адаптируем для братской аудитории.

### Зачем?
- Чтобы приглашение для друзей ("ахишек") выглядело более строго, современно и концептуально, отличаясь от семейного уютного дизайна. Возникнет ощущение стильного закрытого мероприятия.

### Что ты получишь?
- Готовую монохромную веб-страницу с новым дизайном (дополнительные `ramadan-ahi.html`, `style-ahi.css`, и `ahi.js`), которую можно сразу рассылать.

### ⚠️ Может ли что-то сломаться?
- Нет, мы сделаем эту страницу отдельно от первой версии, так что семейное приглашение останется нетронутым.

---

# Implementation Plan: 15 Ramadan Akhi Invite
**Project Type:** WEB

## Overview
Create a second version of the Ramadan Invite focused on an "Akhi / Muslim Brothers" aesthetic based on the provided minimalist/monochrome "aura." design reference. The new version will be a separate page hosted on the same domain or distinct files named `ramadan-ahi`. Target date has been adjusted to March 15th per user request.

## User Review Required
> [!IMPORTANT]
> - Do we want this as a separate `ramadan-ahi.html` file in the current repository, or a completely new repository? (Assuming separate HTML file for now so both exist on Firebase Hosting).
> - Since date is March 15th instead of 14th, the countdown script has been adjusted.
> - Please confirm if the address/details remain EXACTLY the same as the base invite.
> - I will use the "aura." geometrical circle as an SVG element in the center.

## Tech Stack
- **HTML5:** Semantic structure (`ramadan-ahi.html`).
- **Vanilla CSS3:** Custom CSS with a new monochrome color palette matching the "aura." reference (`style-ahi.css`).
- **Vanilla JS:** Reuse the existing countdown and JS logic, adjusted for the new target date (March 15) (`ahi.js`).

## Proposed Changes

### 1. New File Structure
#### [NEW] [ramadan-ahi.html](file:///home/yqecea/coding projects/ramadan_invite/ramadan-ahi.html)
- A streamlined, single-page structure without the floral/watercolor elements.
- Clean typography and ample white space mapping the reference closely.

#### [NEW] [style-ahi.css](file:///home/yqecea/coding projects/ramadan_invite/style-ahi.css)
- New CSS file for the Akhi version to avoid clashing with the original CSS.
- **Palette from reference:**
  - White: `#FFFFFF`
  - Stone Gray: `#AFAEA9`
  - Night Sky Gray: `#8C8F91`
  - Ebony / Invert Black: `#18181A` / `#222`
- **Typography:** Sleek sans-serif (e.g., Inter, Neue Haas Grotesk, or Helvetica) replacing the Cormorant Infant serif font.
- Includes the geometric circle logo from the reference.

#### [NEW] [ahi.js](file:///home/yqecea/coding projects/ramadan_invite/ahi.js)
- Clone of the countdown logic, setting the date to March 15, 2026.

## Task Breakdown (Orchestration Phase 2)

| Task ID | Component | Agent | Description | Verify |
|---|---|---|---|---|
| T1 | Assets | `frontend-specialist` | Recreate the geometric "aura." circle pattern in SVG. | SVGs render sharply across sizes |
| T2 | Structure | `frontend-specialist` | Scaffold `ramadan-ahi.html` with semantic tags, including the new date (March 15th). | HTML is valid and semantic |
| T3 | Styling | `frontend-specialist` | Implement `style-ahi.css` using the strict 4-color palette, sans-serif typography, hover states and smooth entry animations. | Clean monochrome design, 100 on Lighthouse UX |
| T4 | Logic | `frontend-specialist` | Implement `ahi.js` countdown to target March 15. | Timer ticks correctly targeting Mar 15th |

## Phase X: Verification
### Automated & Manual Checks
- [ ] Run `python .agent/scripts/checklist.py .` - Linting, schema, general checks
- [ ] Run UI/UX Audit on the new HTML files
- [ ] Manually check mobile view for safe area constraints, typography hierarchies, and dark mode contrasts
- [ ] Validate that the countdown explicitly targets the 15th of March and successfully ticks down
