"use client";

import { useEffect, useMemo, useState } from "react";

type Screen = "today" | "food" | "movement" | "sleep" | "health";
type State = {
  water: number;
  meals: boolean[];
  movement: number;
  sleepHours: number | null;
  weight: number;
  feeling: string;
};

const STORAGE_KEY = "mybh-flow-next-v1";
const initialState: State = {
  water: 0,
  meals: [false, false, false, false],
  movement: 0,
  sleepHours: null,
  weight: 82,
  feeling: "טוב",
};

const meals = [
  "ארוחה ראשונה · 11:00–12:00",
  "ארוחת ביניים · לפי רעב",
  "ארוחה עיקרית · אחרי אימון",
  "ארוחת ערב · עד 18:30 כשאפשר",
];

export default function Home() {
  const [screen, setScreen] = useState<Screen>("today");
  const [state, setState] = useState<State>(initialState);
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) setState({ ...initialState, ...JSON.parse(saved) });
    setHydrated(true);
  }, []);

  useEffect(() => {
    if (hydrated) localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  }, [state, hydrated]);

  const completedMeals = state.meals.filter(Boolean).length;
  const score = useMemo(() => {
    const water = Math.min(1, state.water / 2500);
    const food = completedMeals / 4;
    const movement = Math.min(1, state.movement / 25);
    const sleep = state.sleepHours ? Math.min(1, state.sleepHours / 7) : 0;
    return Math.round(((water + food + movement + sleep) / 4) * 100);
  }, [state, completedMeals]);

  const card = "rounded-[22px] border border-[var(--line)] bg-white p-4 shadow-[0_6px_24px_rgba(24,63,49,.04)]";
  const button = "rounded-2xl px-4 py-3 font-bold";

  return (
    <main className="mx-auto min-h-screen max-w-[760px] px-3 pb-24 pt-4">
      <header className="mb-4 flex items-center justify-between">
        <div><small className="font-extrabold tracking-[.18em] text-[var(--brand-2)]">MYBH</small><h1 className="m-0 text-2xl font-bold">Flow</h1></div>
        <span className="rounded-full bg-[var(--brand)] px-3 py-2 text-xs text-white">עוז</span>
      </header>

      {screen === "today" && <section className="space-y-3">
        <div className={`${card} border-0 bg-gradient-to-br from-[var(--brand)] to-[var(--brand-2)] text-white`}><small>היום שלך</small><h2 className="text-2xl font-bold">שלום עוז 👋</h2><p className="text-green-50">התקדמות רגועה ועקבית: מים, אוכל מסודר, תנועה ושינה טובה.</p></div>
        <div className="grid grid-cols-4 gap-2">
          <button className={card} onClick={() => setState(s => ({...s, water: s.water + 250}))}>💧<small className="mt-1 block">250 מ״ל</small></button>
          <button className={card} onClick={() => setScreen("food")}>🍽️<small className="mt-1 block">ארוחה</small></button>
          <button className={card} onClick={() => setScreen("movement")}>🚶<small className="mt-1 block">תנועה</small></button>
          <button className={card} onClick={() => setScreen("sleep")}>😴<small className="mt-1 block">שינה</small></button>
        </div>
        <div className={card}><div className="flex justify-between"><h3 className="font-bold">המדדים להיום</h3><b>{score}%</b></div><div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
          <Metric value={`${state.water} / 2500`} label="מים במ״ל" />
          <Metric value={`${completedMeals} / 4`} label="ארוחות" />
          <Metric value={`${state.movement} דק׳`} label="תנועה" />
          <Metric value={state.sleepHours ? `${state.sleepHours}` : "—"} label="שעות שינה" />
        </div></div>
        <div className={card}><h3 className="font-bold">מה עכשיו?</h3><p className="text-[var(--muted)]">{state.water < 1500 ? "לשתות מים ולהתקדם לעבר היעד היומי." : completedMeals < 3 ? "לשמור על הארוחה הבאה מסודרת." : state.movement < 25 ? "להשלים עוד כמה דקות תנועה." : "היום מתקדם מצוין. כדאי לשמור גם על שעת שינה טובה."}</p></div>
      </section>}

      {screen === "food" && <section className="space-y-3"><div className={card}><h2 className="text-xl font-bold">תזונה יומית</h2><p className="text-[var(--muted)]">סמן את הארוחות שבוצעו. בשלב הבא הנתונים יישמרו ב־Supabase.</p></div>{meals.map((meal, i) => <button key={meal} className={`${card} flex w-full items-center justify-between text-right`} onClick={() => setState(s => ({...s, meals: s.meals.map((v, x) => x === i ? !v : v)}))}><span>{meal}</span><b>{state.meals[i] ? "✓" : "○"}</b></button>)}</section>}

      {screen === "movement" && <section className="space-y-3"><div className={card}><h2 className="text-xl font-bold">תנועה ואימון</h2><p className="text-[var(--muted)]">יעד יומי: 25 דקות.</p><div className="mt-4 flex gap-2"><button className={`${button} bg-[var(--soft)]`} onClick={() => setState(s => ({...s, movement: s.movement + 5}))}>+5 דקות</button><button className={`${button} bg-[var(--brand)] text-white`} onClick={() => setState(s => ({...s, movement: 25}))}>סיימתי אימון</button></div></div></section>}

      {screen === "sleep" && <SleepCard card={card} onSave={(hours) => setState(s => ({...s, sleepHours: hours}))} />}

      {screen === "health" && <section className="space-y-3"><div className={card}><h2 className="text-xl font-bold">בריאות ומעקב</h2><label className="mb-3 block">משקל<input className="mt-1 w-full rounded-xl border p-3" type="number" step="0.1" value={state.weight} onChange={e => setState(s => ({...s, weight: Number(e.target.value)}))} /></label><label className="block">איך הגוף מרגיש<select className="mt-1 w-full rounded-xl border p-3" value={state.feeling} onChange={e => setState(s => ({...s, feeling: e.target.value}))}><option>מצוין</option><option>טוב</option><option>בינוני</option><option>עייף</option><option>כואב</option></select></label></div><div className={card}><h3 className="font-bold">Health Connect</h3><p className="text-[var(--muted)]">החיבור בפועל יתווסף במעטפת Android. התשתית נשמרת כשלב אינטגרציה נפרד.</p></div></section>}

      <nav className="fixed bottom-0 left-1/2 grid w-full max-w-[760px] -translate-x-1/2 grid-cols-5 border-t bg-white p-2 text-xs">
        <Nav label="היום" icon="🏠" active={screen === "today"} onClick={() => setScreen("today")} />
        <Nav label="תזונה" icon="🍽️" active={screen === "food"} onClick={() => setScreen("food")} />
        <Nav label="תנועה" icon="🚶" active={screen === "movement"} onClick={() => setScreen("movement")} />
        <Nav label="שינה" icon="😴" active={screen === "sleep"} onClick={() => setScreen("sleep")} />
        <Nav label="בריאות" icon="❤️" active={screen === "health"} onClick={() => setScreen("health")} />
      </nav>
    </main>
  );
}

function Metric({ value, label }: { value: string; label: string }) { return <div className="rounded-2xl bg-[#f8faf9] p-3"><b className="block text-lg">{value}</b><small className="text-[var(--muted)]">{label}</small></div>; }
function Nav({ label, icon, active, onClick }: { label: string; icon: string; active: boolean; onClick: () => void }) { return <button className={active ? "font-extrabold text-[var(--brand)]" : "text-[var(--muted)]"} onClick={onClick}><span className="block text-xl">{icon}</span>{label}</button>; }
function SleepCard({ card, onSave }: { card: string; onSave: (hours: number) => void }) {
  const [start, setStart] = useState("00:00"); const [end, setEnd] = useState("07:00");
  function save() { const [sh, sm] = start.split(":").map(Number); const [eh, em] = end.split(":").map(Number); let mins = eh * 60 + em - (sh * 60 + sm); if (mins <= 0) mins += 1440; onSave(Math.round(mins / 6) / 10); }
  return <section><div className={card}><h2 className="text-xl font-bold">מעקב שינה</h2><label className="mb-3 block">שעת שינה<input className="mt-1 w-full rounded-xl border p-3" type="time" value={start} onChange={e => setStart(e.target.value)} /></label><label className="mb-3 block">שעת קימה<input className="mt-1 w-full rounded-xl border p-3" type="time" value={end} onChange={e => setEnd(e.target.value)} /></label><button className="w-full rounded-2xl bg-[var(--brand)] p-3 font-bold text-white" onClick={save}>שמירת השינה</button></div></section>;
}
