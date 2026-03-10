import { useState, useMemo } from "react";
import {
  LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, Cell, PieChart, Pie, Legend
} from "recharts";

const DATA = {"summary":{"total_revenue":419809.8,"total_orders":2000,"unique_customers":723,"avg_order_value":209.9,"repeat_rate":72.5},"monthly":[{"month":"2022-01","revenue":23180.49,"orders":108,"customers":98},{"month":"2022-02","revenue":19599.32,"orders":94,"customers":91},{"month":"2022-03","revenue":26463.24,"orders":117,"customers":103},{"month":"2022-04","revenue":23768.66,"orders":112,"customers":105},{"month":"2022-05","revenue":27999.57,"orders":123,"customers":110},{"month":"2022-06","revenue":24762.12,"orders":116,"customers":106},{"month":"2022-07","revenue":24418.53,"orders":119,"customers":109},{"month":"2022-08","revenue":17157.9,"orders":93,"customers":87},{"month":"2022-09","revenue":19753.12,"orders":99,"customers":94},{"month":"2022-10","revenue":22467.8,"orders":104,"customers":92},{"month":"2022-11","revenue":24627.28,"orders":117,"customers":106},{"month":"2022-12","revenue":21594.7,"orders":98,"customers":93},{"month":"2023-01","revenue":26799.76,"orders":128,"customers":119},{"month":"2023-02","revenue":20616.53,"orders":99,"customers":92},{"month":"2023-03","revenue":22812.19,"orders":110,"customers":98},{"month":"2023-04","revenue":22862.81,"orders":113,"customers":103},{"month":"2023-05","revenue":24659.75,"orders":121,"customers":107},{"month":"2023-06","revenue":24611.46,"orders":120,"customers":109},{"month":"2023-07","revenue":1654.57,"orders":9,"customers":9}],"categories":[{"category":"Electronics","revenue":55355.77,"orders":190},{"category":"Toys","revenue":45339.65,"orders":216},{"category":"Books","revenue":43919.52,"orders":211},{"category":"Health","revenue":42815.25,"orders":208},{"category":"Food & Drink","revenue":40203.73,"orders":205},{"category":"Automotive","revenue":38803.03,"orders":195},{"category":"Home & Garden","revenue":38764.51,"orders":198},{"category":"Sports","revenue":38564.98,"orders":189},{"category":"Fashion","revenue":38215.02,"orders":192},{"category":"Beauty","revenue":37828.34,"orders":196}],"states":[{"state":"BA","city":"Salvador","revenue":50144.73},{"state":"PR","city":"Curitiba","revenue":48663.46},{"state":"SC","city":"Florianópolis","revenue":45454.24},{"state":"PE","city":"Recife","revenue":44257.74},{"state":"RS","city":"Porto Alegre","revenue":42152.24},{"state":"MG","city":"Belo Horizonte","revenue":40489.73},{"state":"RJ","city":"Rio de Janeiro","revenue":39147.01},{"state":"ES","city":"Vitória","revenue":38619.89},{"state":"GO","city":"Goiânia","revenue":38503.56},{"state":"SP","city":"São Paulo","revenue":32377.2}],"cohort_retention":[{"cohort":"2022-01","size":98,"retention":[100.0,10.2,7.1,14.3,14.3,15.3,8.2,10.2,9.2,10.2,17.3,12.2,15.3,10.2,9.2,15.3,15.3,17.3,3.1]},{"cohort":"2022-02","size":81,"retention":[null,100.0,12.3,14.8,8.6,14.8,18.5,9.9,13.6,8.6,13.6,16.0,16.0,18.5,17.3,8.6,13.6,13.6,1.2]},{"cohort":"2022-03","size":86,"retention":[null,null,100.0,11.6,19.8,9.3,11.6,9.3,9.3,8.1,19.8,10.5,17.4,9.3,11.6,16.3,17.4,11.6,0.0]},{"cohort":"2022-04","size":69,"retention":[null,null,null,100.0,14.5,18.8,18.8,13.0,20.3,13.0,21.7,13.0,10.1,14.5,10.1,11.6,27.5,14.5,1.4]},{"cohort":"2022-05","size":62,"retention":[null,null,null,null,100.0,12.9,12.9,11.3,12.9,22.6,12.9,17.7,19.4,11.3,17.7,17.7,6.5,12.9,0.0]},{"cohort":"2022-06","size":50,"retention":[null,null,null,null,null,100.0,14.0,12.0,10.0,6.0,22.0,16.0,18.0,12.0,14.0,22.0,4.0,18.0,2.0]},{"cohort":"2022-07","size":48,"retention":[null,null,null,null,null,null,100.0,4.2,6.2,14.6,8.3,12.5,10.4,10.4,18.8,14.6,10.4,20.8,0.0]},{"cohort":"2022-08","size":37,"retention":[null,null,null,null,null,null,null,100.0,16.2,18.9,13.5,10.8,13.5,13.5,5.4,10.8,13.5,10.8,2.7]},{"cohort":"2022-09","size":30,"retention":[null,null,null,null,null,null,null,null,100.0,13.3,6.7,6.7,3.3,6.7,16.7,0.0,10.0,3.3,3.3]},{"cohort":"2022-10","size":24,"retention":[null,null,null,null,null,null,null,null,null,100.0,4.2,8.3,20.8,12.5,8.3,8.3,8.3,4.2,0.0]},{"cohort":"2022-11","size":15,"retention":[null,null,null,null,null,null,null,null,null,null,100.0,20.0,13.3,6.7,6.7,20.0,0.0,13.3,0.0]},{"cohort":"2022-12","size":14,"retention":[null,null,null,null,null,null,null,null,null,null,null,100.0,21.4,14.3,7.1,7.1,0.0,7.1,0.0]}],"all_months":["2022-01","2022-02","2022-03","2022-04","2022-05","2022-06","2022-07","2022-08","2022-09","2022-10","2022-11","2022-12","2023-01","2023-02","2023-03","2023-04","2023-05","2023-06","2023-07"],"payment":[{"type":"credit_card","count":511},{"type":"boleto","count":508},{"type":"debit_card","count":501},{"type":"voucher","count":480}],"ltv_dist":{"1":199,"2-3":321,"4-6":180,"7+":23}};

const ACCENT = "#22d3a5";
const ACCENT2 = "#f97316";
const ACCENT3 = "#818cf8";
const BG = "#0b0f1a";
const CARD = "#111827";
const BORDER = "#1f2a3a";
const TEXT = "#e2e8f0";
const MUTED = "#64748b";

const fmt = (n) => n >= 1000 ? `R$ ${(n/1000).toFixed(1)}k` : `R$ ${n.toFixed(0)}`;
const fmtFull = (n) => `R$ ${n.toLocaleString("pt-BR", {minimumFractionDigits:2})}`;

const TABS = ["Overview", "Categories", "Regions", "Cohort Retention", "Customer LTV"];

const CAT_COLORS = ["#22d3a5","#34d399","#6ee7b7","#f97316","#fb923c","#fdba74","#818cf8","#a78bfa","#c4b5fd","#f472b6"];

function KPICard({ label, value, sub, accent }) {
  return (
    <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px", flex: 1, minWidth: 140 }}>
      <div style={{ fontSize: 11, color: MUTED, textTransform: "uppercase", letterSpacing: "0.1em", marginBottom: 8, fontFamily: "monospace" }}>{label}</div>
      <div style={{ fontSize: 28, fontWeight: 700, color: accent || ACCENT, fontFamily: "'DM Mono', monospace", lineHeight: 1 }}>{value}</div>
      {sub && <div style={{ fontSize: 12, color: MUTED, marginTop: 6 }}>{sub}</div>}
    </div>
  );
}

function SectionTitle({ children, note }) {
  return (
    <div style={{ marginBottom: 16, display: "flex", alignItems: "baseline", gap: 12 }}>
      <span style={{ fontSize: 14, fontWeight: 700, color: TEXT, textTransform: "uppercase", letterSpacing: "0.08em", fontFamily: "monospace" }}>{children}</span>
      {note && <span style={{ fontSize: 11, color: MUTED }}>{note}</span>}
    </div>
  );
}

const CustomTooltip = ({ active, payload, label, prefix = "R$" }) => {
  if (!active || !payload?.length) return null;
  return (
    <div style={{ background: "#1e293b", border: `1px solid ${BORDER}`, borderRadius: 8, padding: "10px 14px", fontSize: 12, color: TEXT }}>
      <div style={{ color: MUTED, marginBottom: 4 }}>{label}</div>
      {payload.map((p, i) => (
        <div key={i} style={{ color: p.color || ACCENT }}>
          {p.name}: {typeof p.value === "number" && p.name?.toLowerCase().includes("rev") ? fmtFull(p.value) : p.value}
        </div>
      ))}
    </div>
  );
};

function OverviewTab() {
  const monthly = DATA.monthly.slice(0, 18);
  const [metric, setMetric] = useState("revenue");
  const metricColor = metric === "revenue" ? ACCENT : metric === "orders" ? ACCENT2 : ACCENT3;

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
      <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
        <KPICard label="Total Revenue" value={`R$ ${(DATA.summary.total_revenue/1000).toFixed(1)}k`} sub="Jan 2022 – Jun 2023" />
        <KPICard label="Total Orders" value={DATA.summary.total_orders.toLocaleString()} sub="18-month period" accent={ACCENT2} />
        <KPICard label="Unique Customers" value={DATA.summary.unique_customers} sub="Active buyers" accent={ACCENT3} />
        <KPICard label="Avg Order Value" value={`R$ ${DATA.summary.avg_order_value}`} sub="Per transaction" accent="#f472b6" />
        <KPICard label="Repeat Rate" value={`${DATA.summary.repeat_rate}%`} sub="2+ orders placed" accent="#fbbf24" />
      </div>

      <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
          <SectionTitle note="Monthly, Jan 2022 – Jun 2023">Monthly Trend</SectionTitle>
          <div style={{ display: "flex", gap: 6 }}>
            {["revenue","orders","customers"].map(m => (
              <button key={m} onClick={() => setMetric(m)} style={{
                fontSize: 11, padding: "4px 10px", borderRadius: 6, cursor: "pointer", fontFamily: "monospace",
                background: metric === m ? (m === "revenue" ? ACCENT : m === "orders" ? ACCENT2 : ACCENT3) : "transparent",
                color: metric === m ? "#000" : MUTED,
                border: `1px solid ${metric === m ? "transparent" : BORDER}`
              }}>{m}</button>
            ))}
          </div>
        </div>
        <ResponsiveContainer width="100%" height={220}>
          <LineChart data={monthly} margin={{ top: 4, right: 8, bottom: 0, left: 0 }}>
            <CartesianGrid stroke={BORDER} strokeDasharray="3 3" vertical={false} />
            <XAxis dataKey="month" tick={{ fill: MUTED, fontSize: 10, fontFamily: "monospace" }} axisLine={false} tickLine={false} />
            <YAxis tick={{ fill: MUTED, fontSize: 10, fontFamily: "monospace" }} axisLine={false} tickLine={false}
              tickFormatter={v => metric === "revenue" ? `R$${(v/1000).toFixed(0)}k` : v} />
            <Tooltip content={<CustomTooltip />} />
            <Line type="monotone" dataKey={metric} stroke={metricColor} strokeWidth={2.5} dot={false} activeDot={{ r: 5, fill: metricColor }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px" }}>
        <SectionTitle note="Top 3 months by revenue">Revenue Highlights</SectionTitle>
        <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
          {[...monthly].sort((a,b) => b.revenue - a.revenue).slice(0,3).map((m, i) => (
            <div key={m.month} style={{ flex: 1, minWidth: 120, background: "#1e293b", borderRadius: 8, padding: "12px 16px" }}>
              <div style={{ fontSize: 10, color: MUTED, fontFamily: "monospace", marginBottom: 4 }}>#{i+1}</div>
              <div style={{ fontSize: 16, fontWeight: 700, color: ACCENT, fontFamily: "monospace" }}>{m.month}</div>
              <div style={{ fontSize: 13, color: TEXT, marginTop: 4 }}>{fmtFull(m.revenue)}</div>
              <div style={{ fontSize: 11, color: MUTED }}>{m.orders} orders · {m.customers} buyers</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function CategoriesTab() {
  const [view, setView] = useState("revenue");
  const data = DATA.categories.map(c => ({
    ...c,
    aov: Math.round(c.revenue / c.orders)
  })).sort((a,b) => b[view] - a[view]);

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
      <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20 }}>
          <SectionTitle>Category Performance</SectionTitle>
          <div style={{ display: "flex", gap: 6 }}>
            {["revenue","orders","aov"].map(m => (
              <button key={m} onClick={() => setView(m)} style={{
                fontSize: 11, padding: "4px 10px", borderRadius: 6, cursor: "pointer", fontFamily: "monospace",
                background: view === m ? ACCENT : "transparent",
                color: view === m ? "#000" : MUTED,
                border: `1px solid ${view === m ? "transparent" : BORDER}`
              }}>{m === "aov" ? "AOV" : m}</button>
            ))}
          </div>
        </div>
        <ResponsiveContainer width="100%" height={280}>
          <BarChart data={data} layout="vertical" margin={{ left: 16, right: 16 }}>
            <CartesianGrid stroke={BORDER} strokeDasharray="3 3" horizontal={false} />
            <XAxis type="number" tick={{ fill: MUTED, fontSize: 10, fontFamily: "monospace" }} axisLine={false} tickLine={false}
              tickFormatter={v => view === "revenue" || view === "aov" ? `R$${(v/1000).toFixed(0)}k` : v} />
            <YAxis type="category" dataKey="category" tick={{ fill: TEXT, fontSize: 11, fontFamily: "monospace" }} axisLine={false} tickLine={false} width={90} />
            <Tooltip content={<CustomTooltip />} />
            <Bar dataKey={view} radius={[0, 4, 4, 0]}>
              {data.map((_, i) => <Cell key={i} fill={CAT_COLORS[i % CAT_COLORS.length]} />)}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div style={{ display: "flex", gap: 24, flexWrap: "wrap" }}>
        <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px", flex: 2, minWidth: 280 }}>
          <SectionTitle>Revenue Share</SectionTitle>
          <ResponsiveContainer width="100%" height={220}>
            <PieChart>
              <Pie data={DATA.categories} dataKey="revenue" nameKey="category" cx="50%" cy="50%" outerRadius={80} innerRadius={40}>
                {DATA.categories.map((_, i) => <Cell key={i} fill={CAT_COLORS[i]} />)}
              </Pie>
              <Tooltip formatter={(v) => fmtFull(v)} />
              <Legend wrapperStyle={{ fontSize: 11, fontFamily: "monospace", color: MUTED }} />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px", flex: 1, minWidth: 200 }}>
          <SectionTitle>Key Insights</SectionTitle>
          <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
            {[
              { label: "Top Category", val: "Electronics", sub: `R$ ${(55355.77/1000).toFixed(1)}k revenue`, color: CAT_COLORS[0] },
              { label: "Most Orders", val: "Toys", sub: "216 transactions", color: CAT_COLORS[1] },
              { label: "Highest AOV", val: "Electronics", sub: `R$ ${Math.round(55355.77/190)} avg`, color: ACCENT2 },
              { label: "Lowest Revenue", val: "Beauty", sub: `R$ ${(37828.34/1000).toFixed(1)}k`, color: MUTED },
            ].map(item => (
              <div key={item.label} style={{ borderLeft: `3px solid ${item.color}`, paddingLeft: 12 }}>
                <div style={{ fontSize: 10, color: MUTED, fontFamily: "monospace", textTransform: "uppercase" }}>{item.label}</div>
                <div style={{ fontSize: 14, fontWeight: 600, color: TEXT }}>{item.val}</div>
                <div style={{ fontSize: 11, color: MUTED }}>{item.sub}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function RegionsTab() {
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
      <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px" }}>
        <SectionTitle note="Revenue by Brazilian state">Regional Revenue Breakdown</SectionTitle>
        <ResponsiveContainer width="100%" height={280}>
          <BarChart data={DATA.states} margin={{ left: 8, right: 8 }}>
            <CartesianGrid stroke={BORDER} strokeDasharray="3 3" vertical={false} />
            <XAxis dataKey="state" tick={{ fill: MUTED, fontSize: 11, fontFamily: "monospace" }} axisLine={false} tickLine={false} />
            <YAxis tick={{ fill: MUTED, fontSize: 10, fontFamily: "monospace" }} axisLine={false} tickLine={false}
              tickFormatter={v => `R$${(v/1000).toFixed(0)}k`} />
            <Tooltip content={({ active, payload, label }) => {
              if (!active || !payload?.length) return null;
              const d = DATA.states.find(s => s.state === label);
              return (
                <div style={{ background: "#1e293b", border: `1px solid ${BORDER}`, borderRadius: 8, padding: "10px 14px", fontSize: 12, color: TEXT }}>
                  <div style={{ color: ACCENT, fontWeight: 700 }}>{d?.city} ({label})</div>
                  <div>Revenue: {fmtFull(payload[0].value)}</div>
                </div>
              );
            }} />
            <Bar dataKey="revenue" radius={[4, 4, 0, 0]}>
              {DATA.states.map((_, i) => <Cell key={i} fill={i === 0 ? ACCENT : i === 1 ? ACCENT2 : `${ACCENT}${Math.round(255 * (1 - i * 0.08)).toString(16).padStart(2,'0')}`} />)}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
        {DATA.states.map((s, i) => (
          <div key={s.state} style={{
            background: CARD, border: `1px solid ${i < 3 ? ACCENT + "44" : BORDER}`,
            borderRadius: 10, padding: "14px 18px", flex: 1, minWidth: 130
          }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 4 }}>
              <span style={{ fontSize: 20, fontWeight: 800, color: i < 3 ? ACCENT : MUTED, fontFamily: "monospace" }}>{s.state}</span>
              {i < 3 && <span style={{ fontSize: 10, color: ACCENT, border: `1px solid ${ACCENT}44`, borderRadius: 4, padding: "2px 6px", fontFamily: "monospace" }}>TOP</span>}
            </div>
            <div style={{ fontSize: 11, color: MUTED, marginBottom: 6 }}>{s.city}</div>
            <div style={{ fontSize: 14, fontWeight: 600, color: TEXT, fontFamily: "monospace" }}>
              R$ {(s.revenue / 1000).toFixed(1)}k
            </div>
            <div style={{ marginTop: 8, height: 3, background: BORDER, borderRadius: 2 }}>
              <div style={{ height: "100%", width: `${(s.revenue / DATA.states[0].revenue * 100).toFixed(0)}%`, background: i < 3 ? ACCENT : MUTED, borderRadius: 2 }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function CohortTab() {
  const months = DATA.all_months.slice(0, 13);
  const cohorts = DATA.cohort_retention;

  const getColor = (val) => {
    if (val === null) return "transparent";
    if (val === 100) return "#22d3a5";
    if (val >= 20) return "#16a34a";
    if (val >= 12) return "#4ade80";
    if (val >= 6) return "#86efac";
    if (val > 0) return "#bbf7d0";
    return "#1f2a3a";
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
      <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px" }}>
        <SectionTitle note="% of cohort who ordered again in each subsequent month">Customer Cohort Retention Heatmap</SectionTitle>
        <div style={{ overflowX: "auto" }}>
          <table style={{ borderCollapse: "separate", borderSpacing: 3, fontFamily: "monospace", fontSize: 11, width: "100%" }}>
            <thead>
              <tr>
                <th style={{ color: MUTED, padding: "4px 8px", textAlign: "left", fontWeight: 400 }}>Cohort</th>
                <th style={{ color: MUTED, padding: "4px 8px", textAlign: "center", fontWeight: 400 }}>Size</th>
                {months.map((m, i) => (
                  <th key={m} style={{ color: MUTED, padding: "4px 6px", textAlign: "center", fontWeight: 400, fontSize: 10 }}>
                    M+{i}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {cohorts.map(row => (
                <tr key={row.cohort}>
                  <td style={{ color: TEXT, padding: "3px 8px", fontWeight: 600 }}>{row.cohort}</td>
                  <td style={{ color: MUTED, padding: "3px 8px", textAlign: "center" }}>{row.size}</td>
                  {months.map((_, i) => {
                    const val = row.retention[i];
                    return (
                      <td key={i} title={val !== null ? `${val}%` : "—"} style={{
                        background: getColor(val),
                        borderRadius: 4,
                        padding: "5px 6px",
                        textAlign: "center",
                        color: val === 100 ? "#000" : val > 0 ? "#064e3b" : "transparent",
                        fontWeight: val === 100 ? 700 : 400,
                        minWidth: 36,
                        fontSize: 10
                      }}>
                        {val !== null ? (val === 100 ? "100" : val.toFixed(0)) : ""}
                      </td>
                    );
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div style={{ marginTop: 12, display: "flex", alignItems: "center", gap: 8 }}>
          <span style={{ fontSize: 10, color: MUTED }}>Low</span>
          {["#1f2a3a","#bbf7d0","#86efac","#4ade80","#16a34a","#22d3a5"].map(c => (
            <div key={c} style={{ width: 20, height: 10, background: c, borderRadius: 2 }} />
          ))}
          <span style={{ fontSize: 10, color: MUTED }}>High</span>
        </div>
      </div>

      <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px" }}>
        <SectionTitle note="M+1 return rate per cohort">Month-1 Retention by Cohort</SectionTitle>
        <ResponsiveContainer width="100%" height={180}>
          <BarChart data={cohorts.map(c => ({ cohort: c.cohort, m1: c.retention.find((v, i) => i > 0 && v !== null) || 0 }))}>
            <CartesianGrid stroke={BORDER} strokeDasharray="3 3" vertical={false} />
            <XAxis dataKey="cohort" tick={{ fill: MUTED, fontSize: 10, fontFamily: "monospace" }} axisLine={false} tickLine={false} />
            <YAxis tick={{ fill: MUTED, fontSize: 10, fontFamily: "monospace" }} axisLine={false} tickLine={false}
              tickFormatter={v => `${v}%`} domain={[0, 25]} />
            <Tooltip formatter={(v) => `${v}%`} />
            <Bar dataKey="m1" radius={[4, 4, 0, 0]} fill={ACCENT} />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

function LTVTab() {
  const ltv = [
    { segment: "One-time", key: "1", count: DATA.ltv_dist["1"], color: MUTED },
    { segment: "Occasional (2–3)", key: "2-3", count: DATA.ltv_dist["2-3"], color: ACCENT3 },
    { segment: "Loyal (4–6)", key: "4-6", count: DATA.ltv_dist["4-6"], color: ACCENT2 },
    { segment: "Champion (7+)", key: "7+", count: DATA.ltv_dist["7+"], color: ACCENT },
  ];
  const total = ltv.reduce((s, l) => s + l.count, 0);

  const payment = DATA.payment.map(p => ({ ...p, label: p.type.replace("_", " ") }));

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
      <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px" }}>
        <SectionTitle note="Customers segmented by total orders placed">Customer Purchase Frequency Segments</SectionTitle>
        <div style={{ display: "flex", gap: 12, flexWrap: "wrap", marginBottom: 20 }}>
          {ltv.map(seg => (
            <div key={seg.key} style={{ flex: 1, minWidth: 140, background: "#1e293b", borderRadius: 10, padding: "16px 20px", borderLeft: `4px solid ${seg.color}` }}>
              <div style={{ fontSize: 11, color: MUTED, fontFamily: "monospace", textTransform: "uppercase", letterSpacing: "0.05em" }}>{seg.segment}</div>
              <div style={{ fontSize: 32, fontWeight: 800, color: seg.color, fontFamily: "monospace", lineHeight: 1.2, marginTop: 4 }}>{seg.count}</div>
              <div style={{ fontSize: 12, color: MUTED, marginTop: 4 }}>{(seg.count/total*100).toFixed(1)}% of customers</div>
            </div>
          ))}
        </div>
        <ResponsiveContainer width="100%" height={180}>
          <BarChart data={ltv}>
            <CartesianGrid stroke={BORDER} strokeDasharray="3 3" vertical={false} />
            <XAxis dataKey="segment" tick={{ fill: MUTED, fontSize: 11, fontFamily: "monospace" }} axisLine={false} tickLine={false} />
            <YAxis tick={{ fill: MUTED, fontSize: 10, fontFamily: "monospace" }} axisLine={false} tickLine={false} />
            <Tooltip />
            <Bar dataKey="count" radius={[4, 4, 0, 0]}>
              {ltv.map((s, i) => <Cell key={i} fill={s.color} />)}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div style={{ display: "flex", gap: 24, flexWrap: "wrap" }}>
        <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px", flex: 1, minWidth: 260 }}>
          <SectionTitle>Payment Method Split</SectionTitle>
          <ResponsiveContainer width="100%" height={200}>
            <PieChart>
              <Pie data={payment} dataKey="count" nameKey="label" cx="50%" cy="50%" outerRadius={75} innerRadius={35}>
                {payment.map((_, i) => <Cell key={i} fill={[ACCENT, ACCENT2, ACCENT3, "#f472b6"][i]} />)}
              </Pie>
              <Tooltip formatter={(v, n) => [v, n]} />
              <Legend wrapperStyle={{ fontSize: 11, fontFamily: "monospace", color: MUTED }} />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div style={{ background: CARD, border: `1px solid ${BORDER}`, borderRadius: 12, padding: "20px 24px", flex: 1, minWidth: 240 }}>
          <SectionTitle>Business Observations</SectionTitle>
          <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
            {[
              { icon: "◆", color: ACCENT, text: `72.5% repeat rate — strong retention signal for e-commerce` },
              { icon: "◆", color: ACCENT2, text: `44.4% of customers made 2–3 orders (core mid-tier)` },
              { icon: "◆", color: ACCENT3, text: `Champion segment (7+ orders): only 3.2% but highest LTV` },
              { icon: "◆", color: "#f472b6", text: `Payment methods near-equally split — no dominant preference` },
            ].map((obs, i) => (
              <div key={i} style={{ display: "flex", gap: 10, alignItems: "flex-start" }}>
                <span style={{ color: obs.color, fontSize: 10, marginTop: 3 }}>{obs.icon}</span>
                <span style={{ fontSize: 12, color: MUTED, lineHeight: 1.5 }}>{obs.text}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default function App() {
  const [tab, setTab] = useState(0);

  const tabContent = [<OverviewTab />, <CategoriesTab />, <RegionsTab />, <CohortTab />, <LTVTab />];

  return (
    <div style={{ background: BG, minHeight: "100vh", color: TEXT, fontFamily: "'DM Mono', 'Courier New', monospace", padding: "0 0 40px 0" }}>
      <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&display=swap" rel="stylesheet" />

      {/* Header */}
      <div style={{ borderBottom: `1px solid ${BORDER}`, padding: "20px 32px", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <div style={{ fontSize: 11, color: MUTED, textTransform: "uppercase", letterSpacing: "0.15em", marginBottom: 4 }}>Shabbir Kutbuddin · Portfolio Project</div>
          <div style={{ fontSize: 20, fontWeight: 700, color: TEXT }}>
            <span style={{ color: ACCENT }}>▶</span> E-Commerce Sales & Customer Analytics
          </div>
          <div style={{ fontSize: 11, color: MUTED, marginTop: 4 }}>
            Brazilian E-Commerce Dataset · 2,000 orders · 723 customers · Jan 2022 – Jun 2023
          </div>
        </div>
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
          {["SQL", "Python", "Power BI"].map(t => (
            <span key={t} style={{ fontSize: 10, padding: "3px 8px", border: `1px solid ${ACCENT}44`, borderRadius: 4, color: ACCENT, textTransform: "uppercase", letterSpacing: "0.05em" }}>{t}</span>
          ))}
        </div>
      </div>

      {/* Nav */}
      <div style={{ borderBottom: `1px solid ${BORDER}`, padding: "0 32px", display: "flex", gap: 0 }}>
        {TABS.map((t, i) => (
          <button key={t} onClick={() => setTab(i)} style={{
            fontSize: 12, padding: "14px 18px", cursor: "pointer", background: "transparent",
            color: tab === i ? ACCENT : MUTED,
            borderBottom: tab === i ? `2px solid ${ACCENT}` : "2px solid transparent",
            border: "none", borderBottom: tab === i ? `2px solid ${ACCENT}` : "2px solid transparent",
            fontFamily: "monospace", letterSpacing: "0.03em", transition: "color 0.15s"
          }}>{t}</button>
        ))}
      </div>

      {/* Content */}
      <div style={{ padding: "28px 32px" }}>
        {tabContent[tab]}
      </div>

      {/* Footer */}
      <div style={{ padding: "0 32px", borderTop: `1px solid ${BORDER}`, paddingTop: 16, marginTop: 8 }}>
        <div style={{ fontSize: 10, color: MUTED }}>
          Data: Synthetic dataset modelled on Brazilian E-Commerce (Olist) patterns · Analysis by Shabbir Kutbuddin ·
          <span style={{ color: ACCENT }}> github.com/shabbirkutub/ecommerce-analytics</span>
        </div>
      </div>
    </div>
  );
}
