# Mubarak Version Orchestration Plan

## 🎯 ДЛЯ ТЕБЯ (Простым языком)
### Что будет сделано?
- Полностью переработаем дизайн версии Mubarak: вернем светлый "лабораторный" стиль (как в предоставленных примерах Brand Design).
- Уберем лишние технические надписи (перегруженный HUD), чтобы приглашение стало чище и читабельнее.
- Заменим обращение "братья/ахи" на более нейтральное, подходящее для всех гостей.
- Добавим точную инструкцию по входу: код от внешних калиток — #9757#, код от подъезда — #3333.
- Настроим аккуратные блоки для всей информации, оставив строгие линии и крупную типографику.

### Зачем?
Прошлый вариант стал слишком "хакерским" и темным, потеряв читабельность для более взрослой или общей аудитории. Новый стиль (как на референсах Text Laboratory) — это модный, но светлый и понятный "брутализм", который выглядит премиально и не режет глаз.

### Что ты получишь?
Светлую, выверенную до пикселя страницу `ramadan-mubarak.html` с идеальными шрифтами, где сразу понятно куда идти и какие коды вводить, без отвлекающего визуального шума.

### ⚠️ Может ли что-то сломаться?
Нет, мы работаем **ТОЛЬКО** над версией `ramadan-mubarak.html`. Основная версия `invite` останется в безопасности. Изменения сразу же зальем в Firebase.


---

## 🎼 Orchestration Report

### Task
Overhaul UI/UX of Mubarak version based on `brand_design` folder images (Text Laboratory aesthetic). Remove excessive HUD noise, alter specific sibling text ("Братья", "Ахи"), update gate codes (#9757# external, #3333 internal), and finally deploy cleanly while leaving the core `invite` version perfectly intact. User requested immediate execution.

### Mode
edit / orchestrate (Immediate execution requested by user)

### Agents Invoked (MINIMUM 3)
| # | Agent | Focus Area | Status |
|---|-------|------------|--------|
| 1 | `project-planner` | Task breakdown & PLAN.md creation | ✅ |
| 2 | `frontend-specialist` | UI/UX implementation, HTML/CSS brutalist light refactor | Pending |
| 3 | `test-engineer` | Visual diff testing & deployment | Pending |

### Verification Scripts To Execute
- `lint_runner.py` -> Verify HTML/CSS syntax.
- `firebase deploy` -> Push changes to live.

### Key Findings
1. **[project-planner]**: We must strictly target `style-mubarak.css` and `ramadan-mubarak.html`. Brand reference dictates a pale mint/cyan background, stark bold black typography, heavy use of black lines/borders, barcodes, but cleaner layout.

## 🔴 Implementation Steps (Phase 2)
1. **Frontend Specialist:** 
   - Modify `style-mubarak.css`: Change `--bg` to light cyan (`#e8f5f1`), `--text` to black (`#000`), borders to black.
   - Adjust `ramadan-mubarak.html`: Remove overly confusing HUD lines (`.top-hud`, excessive data lines).
   - Update countdown timer to be large black text on light bg, solid borders.
   - Change text "Ассаляму алейкум, братья! Приглашаем..." -> "Ассаляму алейкум! Приглашаем вас разделить благодать священного месяца Рамадан на совместном вечернем ужине Ауызашар."
   - Update Address Details box:
     - "Код от внешних калиток: #9757#"
     - "Код от подъезда: #3333"
   - Invert images/ornaments back to black outlines on light background (no invert/blend overlays needed if original is black, or multiply if they are on a white bg).
2. **Test Engineer:**
   - Launch local server.
   - Take screenshots to verify the aesthetic matches `/tmp/brutal_mubarak1.png` but with cleaner UX and no brothers text.
   - Fix any failing elements.
3. **DevOps Engineer (Deploy):**
   - Run `git add .`, commit changes.
   - Run `firebase deploy --only hosting`.
