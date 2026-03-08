// =============================================
// Ауызашар (Akhi Version) — Script
// =============================================

document.addEventListener('DOMContentLoaded', () => {
    // -- Countdown Timer (Target: March 15, 2026) --
    const target = new Date('2026-03-15T18:00:00+05:00').getTime();
    const els = {
        d: document.getElementById('cd-days'),
        h: document.getElementById('cd-hours'),
        m: document.getElementById('cd-minutes'),
        s: document.getElementById('cd-seconds')
    };

    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function updateVal(el, val) {
        const str = String(val).padStart(2, '0');
        if (el.textContent === str) return;

        if (!reducedMotion) {
            el.classList.add('pop');
            requestAnimationFrame(() => {
                setTimeout(() => {
                    el.textContent = str;
                    el.classList.remove('pop');
                }, 150);
            });
        } else {
            el.textContent = str;
        }
    }

    function tick(initial) {
        const diff = target - Date.now();
        if (diff <= 0) {
            Object.values(els).forEach(e => { e.textContent = '00'; });
            return false;
        }

        const d = Math.floor(diff / 86400000);
        const h = Math.floor((diff % 86400000) / 3600000);
        const m = Math.floor((diff % 3600000) / 60000);
        const s = Math.floor((diff % 60000) / 1000);

        if (initial) {
            els.d.textContent = String(d).padStart(2, '0');
            els.h.textContent = String(h).padStart(2, '0');
            els.m.textContent = String(m).padStart(2, '0');
            els.s.textContent = String(s).padStart(2, '0');
        } else {
            updateVal(els.d, d);
            updateVal(els.h, h);
            updateVal(els.m, m);
            updateVal(els.s, s);
        }
        return true;
    }

    tick(true);
    const interval = setInterval(() => {
        if (!tick(false)) clearInterval(interval);
    }, 1000);

    // -- Scroll Animations --
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        { rootMargin: '0px 0px -40px 0px', threshold: 0.1 }
    );

    document.querySelectorAll('.anim').forEach(el => observer.observe(el));

    // -- Add to Calendar (.ics) --
    document.getElementById('addToCalendar').addEventListener('click', () => {
        const ics = [
            'BEGIN:VCALENDAR',
            'VERSION:2.0',
            'PRODID:-//Bekbolat Akhiy//Invite//RU',
            'CALSCALE:GREGORIAN',
            'METHOD:PUBLISH',
            'BEGIN:VEVENT',
            'DTSTART:20260315T130000Z',
            'DTEND:20260315T170000Z',
            'SUMMARY:Ауызашар | 15 Марта',
            'DESCRIPTION:Братский Ауызашар.\n\nЖдем вас!',
            'LOCATION:Olymp Palace 2\, Керей\, Жәнібек хандар к-сі\, 22\, подъезд 10\, этаж 12\, кв 347\, Астана',
            'GEO:51.128;71.430',
            'STATUS:CONFIRMED',
            'END:VEVENT',
            'END:VCALENDAR'
        ].join('\r\n');

        const blob = new Blob([ics], { type: 'text/calendar;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'auyzashar-ahi-invite.ics';
        a.click();
        URL.revokeObjectURL(url);
    });
});
