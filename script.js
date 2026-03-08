// =============================================
// Қоныстой + Ауызашар — Script
// =============================================

const translations = {
    kk: {
        familyName: 'Бекболат әулеті',
        heroDate: '14 Наурыз 2026, Сенбі',
        inviteText: 'Сіздерді жаңа шаңырағымыздың қуанышы – Қоныстойға және Ауызашар дастарханына қонақ болуға шақырамыз',
        countdownLabel: 'тойға дейін',
        cdDays: 'күн',
        cdHours: 'сағат',
        cdMins: 'минут',
        cdSecs: 'секунд',
        detailDate: '14 наурыз 2026, сенбі',
        detailAddress: 'Керей, Жәнібек хандар к-сі, 22',
        detailFloor: '10 подъезд, 12 қабат, 347 пәтер',
        gateCodeMain: 'Код домофона',
        gateCodeSub: '1877# немесе #9757#',
        footerText: 'Сіздермен кездесуді асыға күтеміз!',
        addCalendar: 'Күнтізбеге қосу',
        contactLabel: 'байланыс'
    },
    ru: {
        familyName: 'Семья Бекболат',
        heroDate: '14 Марта 2026, Суббота',
        inviteText: 'Приглашаем вас разделить радость нашего новоселья — Коныстой и вечерний ужин Ауызашар',
        countdownLabel: 'до торжества',
        cdDays: 'дней',
        cdHours: 'часов',
        cdMins: 'минут',
        cdSecs: 'секунд',
        detailDate: '14 марта 2026, суббота',
        detailAddress: 'Керей, Жанибек хандар ул., 22',
        detailFloor: '10 подъезд, 12 этаж, 347 кв.',
        gateCodeMain: 'Код домофона',
        gateCodeSub: '1877# или #9757#',
        footerText: 'С нетерпением ждём встречи с вами!',
        addCalendar: 'Добавить в календарь',
        contactLabel: 'контакты'
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // -- Language Switcher --
    const langBtns = document.querySelectorAll('.lang-btn');
    const i18nEls = document.querySelectorAll('[data-i18n]');

    function setLang(lang) {
        const dict = translations[lang];
        if (!dict) return;

        langBtns.forEach(b => {
            const active = b.dataset.lang === lang;
            b.classList.toggle('active', active);
            b.setAttribute('aria-pressed', active);
        });

        i18nEls.forEach(el => {
            const key = el.dataset.i18n;
            if (dict[key]) el.textContent = dict[key];
        });

        document.documentElement.lang = lang;
    }

    langBtns.forEach(b => b.addEventListener('click', () => setLang(b.dataset.lang)));

    // -- Countdown Timer --
    const target = new Date('2026-03-14T18:00:00+05:00').getTime();
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
            'PRODID:-//Bekbolat Family//Invite//KK',
            'CALSCALE:GREGORIAN',
            'METHOD:PUBLISH',
            'BEGIN:VEVENT',
            'DTSTART:20260314T130000Z',
            'DTEND:20260314T170000Z',
            'SUMMARY:Қоныстой + Ауызашар | Бекболат әулеті',
            'DESCRIPTION:Қоныстойға және Ауызашар дастарханына қонақ болуға шақырамыз!\n\nНовоселье и Ауызашар — семья Бекболат',
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
        a.download = 'bekbolat-invite.ics';
        a.click();
        URL.revokeObjectURL(url);
    });
});