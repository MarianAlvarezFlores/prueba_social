import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import json

# =========================================================================
# 1. DATOS MAESTROS CONSOLIDADOS (INFORME 24.09)
# =========================================================================
datos_resumen = pd.DataFrame([
    {
        "Tema": "Alcoholemia Viral (Iñaki)",
        "Canal": "Instagram",
        "Volumen": 470000,
        "Interacciones": 21039,
        "Semaforo": "🟢 Oportunidad",
        "Clima": "70% Humor / Empatía",
        "Driver_Clave": "Nerviosismo ('sordo en tiroteo') / Autos clásicos / Dudas VTV"
    },
    {
        "Tema": "Madres del Dolor / Icardi",
        "Canal": "X (Twitter) / IG",
        "Volumen": 85000,
        "Interacciones": 1823,
        "Semaforo": "🟡 Monitoreo",
        "Clima": "65% Crítico (Doble vara / ONGs)",
        "Driver_Clave": "Selectividad institucional ('se cuelgan de Icardi') vs Wanda/Lola Latorre"
    },
    {
        "Tema": "Debate Fotomultas (CABA)",
        "Canal": "X (Twitter)",
        "Volumen": 45000,
        "Interacciones": 850,
        "Semaforo": "🟡 Tensión",
        "Clima": "55% Crítico / 45% Debate",
        "Driver_Clave": "Multa en plata (recaudación) vs Quita de puntos (Scoring)"
    },
    {
        "Tema": "Inspector en Capot (Cba)",
        "Canal": "IG / X",
        "Volumen": 65000,
        "Interacciones": 847,
        "Semaforo": "🔴 Alerta",
        "Clima": "75% Hostil al agente",
        "Driver_Clave": "Rechazo a subirse al capot / Exposición física y falta de protocolo"
    },
    {
        "Tema": "Caso Berisso (Niño moto)",
        "Canal": "Clarín (X) / Telefe (IG)",
        "Volumen": 38000,
        "Interacciones": 620,
        "Semaforo": "🟢 Positivo",
        "Clima": "80% Favorable a sanción",
        "Driver_Clave": "Mención explícita: 'ANSV trabaja para identificar y sancionar'"
    },
    {
        "Tema": "Trámites y Consultas LNC",
        "Canal": "X (Twitter)",
        "Volumen": 25000,
        "Interacciones": 380,
        "Semaforo": "🔵 Servicio",
        "Clima": "80% Neutro / Duda",
        "Driver_Clave": "Plazo de gracia 90 days vs 1 año / Costo profesional en PBA"
    },
    {
        "Tema": "Capacitación Escuelas",
        "Canal": "Instagram",
        "Volumen": 8000,
        "Interacciones": 150,
        "Semaforo": "🟢 Positivo",
        "Clima": "90% Favorable",
        "Driver_Clave": "Acción formativa conjunta ANSV + Estrellas Amarillas en escuelas"
    }
])

marca_font = "Montserrat, sans-serif"
marca_color_bg = "#F9F6F3"
marca_color_accent = "#406576"

# -------------------------------------------------------------
# FIG 1: RESUMEN EJECUTIVO & KPIS
# -------------------------------------------------------------
fig1 = make_subplots(
    rows=3, cols=3,
    specs=[
        [{"type": "indicator"}, {"type": "indicator"}, {"type": "indicator"}],
        [{"colspan": 3, "type": "table"}, None, None],
        [{"colspan": 1, "type": "pie"}, {"colspan": 2, "type": "bar"}, None]
    ],
    row_heights=[0.20, 0.45, 0.35],
    vertical_spacing=0.08,
    horizontal_spacing=0.05
)
fig1.add_trace(go.Indicator(
    mode="number",
    value=datos_resumen["Volumen"].sum(),
    number=dict(valueformat=",.0f", suffix=" views", font=dict(color=marca_color_accent, size=30)),
    title=dict(text="<b>Alcance Total Monitoreado</b><br><span style='font-size:11px;color:#777777'>Suma bruta de los 7 tópicos</span>")
), row=1, col=1)

fig1.add_trace(go.Indicator(
    mode="number",
    value=datos_resumen["Interacciones"].sum(),
    number=dict(valueformat=",.0f", suffix=" interacc.", font=dict(color="#000000", size=30)),
    title=dict(text="<b>Compromiso / Engagement</b><br><span style='font-size:11px;color:#777777'>Likes + Comentarios registrados</span>")
), row=1, col=2)

fig1.add_trace(go.Indicator(
    mode="number",
    value=57,
    number=dict(suffix="%", font=dict(color="#ea580c", size=30)),
    title=dict(text="<b>Polarización Crítica</b><br><span style='font-size:11px;color:#777777'>Tasa de tensión en debates de texto</span>")
), row=1, col=3)

fig1.add_trace(go.Table(
    header=dict(
        values=["<b>Eje / Suceso</b>", "<b>Canal</b>", "<b>Semáforo</b>", "<b>Clima Social</b>", "<b>Driver Clave</b>"],
        fill_color="#000000",
        font=dict(color="#ffffff", size=11, family=marca_font),
        align="left",
        height=28
    ),
    cells=dict(
        values=[
            datos_resumen["Tema"],
            datos_resumen["Canal"],
            datos_resumen["Semaforo"],
            datos_resumen["Clima"],
            datos_resumen["Driver_Clave"]
        ],
        fill_color=[["#FFFFFF", "#F9F6F3"] * 4],
        font=dict(color="#000000", size=10.5, family=marca_font),
        align="left",
        height=25
    )
), row=2, col=1)

fig1.add_trace(go.Pie(
    labels=datos_resumen["Tema"],
    values=datos_resumen["Volumen"],
    hole=0.52,
    marker=dict(colors=[marca_color_accent, "#e11d48", "#f59e0b", "#7c3aed", "#10b981", "#777777", "#38bdf8"]),
    textinfo="percent",
    showlegend=False
), row=3, col=1)

fig1.add_trace(go.Bar(
    y=datos_resumen["Tema"],
    x=datos_resumen["Interacciones"],
    orientation="h",
    marker=dict(color=[marca_color_accent, "#e11d48", "#f59e0b", "#7c3aed", "#10b981", "#777777", "#38bdf8"]),
    text=datos_resumen["Interacciones"],
    textposition="outside",
    showlegend=False
), row=3, col=2)

fig1.update_layout(height=720, margin=dict(t=30, b=20, l=140, r=40), plot_bgcolor=marca_color_bg, paper_bgcolor=marca_color_bg, font=dict(family=marca_font))

# -------------------------------------------------------------
# FIG 2: TREEMAP SEMAFÓRICO COMPLETO
# -------------------------------------------------------------
treemap_df = pd.DataFrame({
    "Tema": [
        "Alcoholemia Viral", "Alcoholemia Viral", "Alcoholemia Viral", "Alcoholemia Viral", "Alcoholemia Viral",
        "Madres del Dolor / Icardi", "Madres del Dolor / Icardi", "Madres del Dolor / Icardi", "Madres del Dolor / Icardi",
        "Debate Fotomultas", "Debate Fotomultas", "Debate Fotomultas", "Debate Fotomultas",
        "Inspector Córdoba", "Inspector Córdoba", "Inspector Córdoba",
        "Caso Berisso", "Caso Berisso",
        "Trámites LNC", "Trámites LNC",
        "Capacitación",
    ],
    "Subtema": [
        "Nerviosismo: 'sordo en tiroteo' (Humor)", "Detención a clásicos", "Dudas VTV y cédula", "Quejas peajes Ruta 2", "Crítica a controles",
        "Doble vara institucional (Selectividad)", "Comunicado ONGs (Iezzi / LAM)", "Jurisdicción Country vs PBA", "Validez registro italiano",
        "Bolsillo vs Quita de puntos", "Sospecha fin recaudatorio", "Reincidencia sin registro", "Tolerancia excesos 3-5 km/h",
        "Rechazo accionar agente (capot)", "Hostilidad a controles municipales", "Demanda sanción penal conductor",
        "Mención positiva intervención ANSV", "Repudio a madre filmando",
        "Confusión prórroga 90 days vs 1 año", "Reclamo costo profesional PBA",
        "Educación vial escuelas (Estrellas)"
    ],
    "Volumen": [18, 6, 5, 5, 2, 12, 8, 4, 3, 8, 6, 4, 2, 8, 5, 3, 6, 4, 4, 2, 3],
    "Sentimiento": [0.85, 0.1, 0.0, -0.6, -0.7, -0.85, -0.75, -0.2, -0.1, -0.1, -0.7, -0.4, -0.55, -0.85, -0.8, 0.2, 0.75, -0.6, 0.0, -0.6, 0.85]
})

fig2 = px.treemap(
    treemap_df,
    path=[px.Constant("Monitoreo Integral (24.09)"), "Tema", "Subtema"],
    values="Volumen",
    color="Sentimiento",
    color_continuous_scale=[[0.0, "#dc2626"], [0.45, "#f59e0b"], [0.6, "#777777"], [1.0, "#16a34a"]],
    color_continuous_midpoint=0.0
)
fig2.update_traces(texttemplate="<b>%{label}</b><br>Share: %{value}%<br>Tono: %{color:.2f}", marker=dict(cornerradius=4))
fig2.update_layout(height=650, margin=dict(t=40, l=15, r=15, b=20), paper_bgcolor=marca_color_bg, font=dict(family=marca_font))

# -------------------------------------------------------------
# FIG 3: RED SEMÁNTICA
# -------------------------------------------------------------
nodes = {
    "ANSV / Operativos": {"pos": (0.0, 0.0), "color": marca_color_accent, "size": 36},
    "Alcoholemia 0": {"pos": (-0.45, 0.55), "color": "#16a34a", "size": 26},
    "Viral Iñaki (Humor)": {"pos": (-0.85, 0.75), "color": "#16a34a", "size": 24},
    "Peajes Ruta 2": {"pos": (-0.95, 0.25), "color": "#f59e0b", "size": 22},
    "Fotomultas": {"pos": (0.65, 0.5), "color": "#f59e0b", "size": 26},
    "Fin Recaudatorio": {"pos": (0.35, 0.9), "color": "#dc2626", "size": 26},
    "Sistema Scoring": {"pos": (0.95, 0.75), "color": "#f59e0b", "size": 22},
    "Madres del Dolor / Icardi": {"pos": (0.7, -0.45), "color": "#f59e0b", "size": 26},
    "Doble Vara / Selectividad": {"pos": (0.95, -0.8), "color": "#dc2626", "size": 24},
    "Caso Berisso (Moto)": {"pos": (0.1, -0.75), "color": "#16a34a", "size": 24},
    "Control Municipal": {"pos": (-0.55, -0.45), "color": "#f59e0b", "size": 24},
    "Inspector Capot (Cba)": {"pos": (-0.85, -0.75), "color": "#dc2626", "size": 26},
    "Falta de Protocolos": {"pos": (-0.35, -0.9), "color": "#dc2626", "size": 22},
    "LNC / Trámites": {"pos": (-0.2, 0.35), "color": marca_color_accent, "size": 24},
    "Dudas Plazo 90 días": {"pos": (-0.4, 0.85), "color": "#f59e0b", "size": 20},
}
edges = [
    ("ANSV / Operativos", "Alcoholemia 0"), ("Alcoholemia 0", "Viral Iñaki (Humor)"),
    ("Viral Iñaki (Humor)", "Peajes Ruta 2"), ("Peajes Ruta 2", "Fin Recaudatorio"),
    ("ANSV / Operativos", "Fotomultas"), ("Fotomultas", "Fin Recaudatorio"),
    ("Fotomultas", "Sistema Scoring"), ("ANSV / Operativos", "Madres del Dolor / Icardi"),
    ("Madres del Dolor / Icardi", "Doble Vara / Selectividad"), ("ANSV / Operativos", "Caso Berisso (Moto)"),
    ("ANSV / Operativos", "Control Municipal"), ("Control Municipal", "Inspector Capot (Cba)"),
    ("Inspector Capot (Cba)", "Falta de Protocolos"), ("ANSV / Operativos", "LNC / Trámites"),
    ("LNC / Trámites", "Dudas Plazo 90 días"), ("LNC / Trámites", "Fin Recaudatorio")
]
edge_x, edge_y = [], []
for src, dst in edges:
    x0, y0 = nodes[src]["pos"]
    x1, y1 = nodes[dst]["pos"]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
edge_trace = go.Scatter(x=edge_x, y=edge_y, line=dict(width=1.5, color="#777777"), hoverinfo="none", mode="lines")
node_x = [nodes[n]["pos"][0] for n in nodes]
node_y = [nodes[n]["pos"][1] for n in nodes]
node_text = list(nodes.keys())
node_color = [nodes[n]["color"] for n in nodes]
node_size = [nodes[n]["size"] for n in nodes]
node_trace = go.Scatter(x=node_x, y=node_y, mode="markers+text", text=node_text, textposition="top center", marker=dict(size=node_size, color=node_color, line=dict(width=2, color="#000")), textfont=dict(size=10.5, color="#000"))
fig3 = go.Figure(data=[edge_trace, node_trace], layout=go.Layout(height=620, showlegend=False, xaxis=dict(showgrid=False, zeroline=False, showticklabels=False), yaxis=dict(showgrid=False, zeroline=False, showticklabels=False), paper_bgcolor=marca_color_bg, plot_bgcolor=marca_color_bg))

# -------------------------------------------------------------
# FIG 4: RADAR DE PERCEPCIÓN
# -------------------------------------------------------------
fig4 = go.Figure(data=go.Scatterpolar(
    r=[85, 40, 45, 30, 35],
    theta=['Cercanía / Empatía', 'Transparencia Normativa', 'Legitimidad Preventiva', 'Profesionalismo Operativo', 'Equidad ante la Ley'],
    fill='toself',
    fillcolor='rgba(64, 101, 118, 0.35)',
    line=dict(color=marca_color_accent, width=2)
))
fig4.update_layout(height=580, polar=dict(radialaxis=dict(visible=True, range=[0, 100])), paper_bgcolor=marca_color_bg, font=dict(family=marca_font))

# -------------------------------------------------------------
# FIG 5: HEATMAP DE TENSIÓN
# -------------------------------------------------------------
drivers_heat = ["Fin Recaudatorio", "Doble Vara / Selectividad", "Falta de Protocolo", "Desinformación", "Empatía / Humor"]
temas_heat = ["Alcoholemia Viral", "Madres del Dolor / Icardi", "Debate Fotomultas", "Inspector Córdoba", "Caso Berisso", "Trámites LNC"]
z_values = [
    [15,  0,  0, 25, 85],
    [ 5, 90, 10, 20,  0],
    [85, 10,  0, 20,  0],
    [40,  0, 95, 10,  5],
    [ 0, 15, 10, 10, 75],
    [30,  0,  0, 80, 15]
]
fig5 = px.imshow(
    z_values,
    labels=dict(x="Driver de Percepción", y="Eje Monitoreado", color="Intensidad"),
    x=drivers_heat,
    y=temas_heat,
    color_continuous_scale=[[0.0, "#FFFFFF"], [0.3, "#F9F6F3"], [0.7, "#406576"], [1.0, "#000000"]],
    text_auto=True,
    aspect="auto"
)
fig5.update_layout(height=550, margin=dict(t=40, l=160, r=40, b=50), paper_bgcolor=marca_color_bg, font=dict(family=marca_font))

# -------------------------------------------------------------
# FIG 6: NET SENTIMENT SCORE (NSS)
# -------------------------------------------------------------
temas_nss = ["Alcoholemia Viral", "Capacitación Escuelas", "Caso Berisso", "Trámites LNC", "Fotomultas CABA", "Madres del Dolor / Icardi", "Inspector Córdoba"]
nss_vals = [65, 80, 20, 0, -55, -60, -70]
colors_nss = ["#16a34a" if x > 0 else "#777777" if x == 0 else "#dc2626" for x in nss_vals]
fig6 = go.Figure(go.Bar(
    x=nss_vals, y=temas_nss, orientation="h",
    text=[f"{x:+d}" for x in nss_vals], textposition="outside",
    marker=dict(color=colors_nss, line=dict(width=1, color="#000"))
))
fig6.update_layout(height=550, xaxis=dict(title="Net Sentiment Score (-100 a +100)", range=[-85, 95], zeroline=True, zerolinewidth=2, zerolinecolor="#000"), paper_bgcolor=marca_color_bg, plot_bgcolor=marca_color_bg, margin=dict(t=40, b=40, l=170, r=40), font=dict(family=marca_font))

# -------------------------------------------------------------
# EXPORTACIÓN AL HTML CON EL BOTÓN PARA VER EL INFORME PDF ORIGINAL
# -------------------------------------------------------------
charts_json = json.dumps([
    json.loads(fig1.to_json()),
    json.loads(fig2.to_json()),
    json.loads(fig3.to_json()),
    json.loads(fig4.to_json()),
    json.loads(fig5.to_json()),
    json.loads(fig6.to_json())
])

html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Dashboard Integral • Compacto Medios</title>
  <script src="https://cdn.plot.ly/plotly-2.30.0.min.js"></script>
  <!-- Enlace al archivo CSS basado en el Manual de Marca -->
  <link rel="stylesheet" href="manual_marca.css">
</head>
<body>
  <div class="header">
    <div>
      <h1>DASHBOARD DE INTELIGENCIA • COMPACTO MEDIOS</h1>
      <p>Monitoreo diario integral • Seguridad Vial • 24.09</p>
    </div>
    <div style="display: flex; gap: 10px; align-items: center;">
      <!-- Botón para ver el informe PDF original -->
      <a href="INFORME DIARIO RRSS - 24.9.pdf" target="_blank" class="badge" style="background-color: #000000; color: #FFFFFF; text-decoration: none; border: 1px solid #406576; display: flex; align-items: center; gap: 6px; padding: 8px 14px; font-weight: 600;">
        📄 Ver Informe PDF Original
      </a>
      <span class="badge">Edición Ejecutiva</span>
    </div>
  </div>

  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab(0)">📊 1. Resumen y Alertas</button>
    <button class="tab-btn" onclick="switchTab(1)">🗂️ 2. Treemap Semafórico</button>
    <button class="tab-btn" onclick="switchTab(2)">🕸️ 3. Red Semántica</button>
    <button class="tab-btn" onclick="switchTab(3)">📡 4. Radar de Percepción</button>
    <button class="tab-btn" onclick="switchTab(4)">🔥 5. Matriz de Tensión</button>
    <button class="tab-btn" onclick="switchTab(5)">⚖️ 6. Balance Neto (NSS)</button>
  </div>

  <div class="tab-content active" id="tab-0">
    <div class="panel-info"><b>Resumen Directivo:</b> Vista macro de la jornada con KPIs de impacto, matriz de alertas operativas, share de atención y volumen de interacción.</div>
    <div id="chart-0"></div>
  </div>
  <div class="tab-content" id="tab-1">
    <div class="panel-info"><b>Treemap Semafórico:</b> Proporción de temas y subtemas. El color indica el clima del discurso según la identidad editorial.</div>
    <div id="chart-1"></div>
  </div>
  <div class="tab-content" id="tab-2">
    <div class="panel-info"><b>Red de Relaciones:</b> Conexiones cognitivas y bifurcación del debate social alrededor de operativos y controversias.</div>
    <div id="chart-2"></div>
  </div>
  <div class="tab-content" id="tab-3">
    <div class="panel-info"><b>Radar de Percepción:</b> Evaluación de 5 atributos institucionales percibidos en las redes durante el día.</div>
    <div id="chart-3"></div>
  </div>
  <div class="tab-content" id="tab-4">
    <div class="panel-info"><b>Matriz de Tensión:</b> Muestra la intensidad con que cada tema activa reclamos específicos de los usuarios.</div>
    <div id="chart-4"></div>
  </div>
  <div class="tab-content" id="tab-5">
    <div class="panel-info"><b>Net Sentiment Score:</b> Balance neto entre comentarios positivos y negativos (% Favorables - % Críticos).</div>
    <div id="chart-5"></div>
  </div>

  <script>
    const figures = """ + charts_json + """;
    function renderPlot(idx) {
      const el = document.getElementById('chart-' + idx);
      if (!el.hasChildNodes()) {
        Plotly.newPlot(el, figures[idx].data, figures[idx].layout, {responsive: true});
      }
    }
    function switchTab(idx) {
      document.querySelectorAll('.tab-btn').forEach((b, i) => {
        b.classList.toggle('active', i === idx);
      });
      document.querySelectorAll('.tab-content').forEach((c, i) => {
        c.classList.toggle('active', i === idx);
      });
      renderPlot(idx);
    }
    renderPlot(0);
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ Archivo index.html actualizado con el botón de acceso al PDF.")
