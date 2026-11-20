"""
Professional UML 2.0 Component Diagram Generator
System: Group Travel Expense Simplification Engine
Domain: Retail, E-Commerce & Finance
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Arc, Rectangle

def draw_component(ax, x, y, w, h, name, stereotype="«component»", bg_color="#EBF3FA", border_color="#1D4E89", text_color="#0F2942"):
    rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.0,rounding_size=0.15",
                          facecolor=bg_color, edgecolor=border_color, linewidth=1.5, zorder=2)
    ax.add_patch(rect)
    
    # UML 2.0 Component Icon in top-right corner
    icon_w, icon_h = 0.55, 0.38
    ix = x + w - icon_w - 0.15
    iy = y + h - icon_h - 0.15
    ax.add_patch(Rectangle((ix, iy), icon_w, icon_h, facecolor="#FFFFFF", edgecolor=border_color, linewidth=1.0, zorder=3))
    tab_w, tab_h = 0.2, 0.09
    ax.add_patch(Rectangle((ix - tab_w/2, iy + icon_h*0.58), tab_w, tab_h, facecolor="#FFFFFF", edgecolor=border_color, linewidth=0.8, zorder=4))
    ax.add_patch(Rectangle((ix - tab_w/2, iy + icon_h*0.16), tab_w, tab_h, facecolor="#FFFFFF", edgecolor=border_color, linewidth=0.8, zorder=4))
    
    # Text
    lines = name.split('\n')
    if len(lines) == 1:
        ax.text(x + w/2, y + h*0.68, stereotype, fontsize=7.5, ha='center', va='center', color="#475569", style='italic', weight='bold', zorder=5)
        ax.text(x + w/2, y + h*0.35, lines[0], fontsize=9, ha='center', va='center', color=text_color, weight='bold', zorder=5)
    elif len(lines) == 2:
        ax.text(x + w/2, y + h*0.72, stereotype, fontsize=7.5, ha='center', va='center', color="#475569", style='italic', weight='bold', zorder=5)
        ax.text(x + w/2, y + h*0.44, lines[0], fontsize=8.5, ha='center', va='center', color=text_color, weight='bold', zorder=5)
        ax.text(x + w/2, y + h*0.22, lines[1], fontsize=8.5, ha='center', va='center', color=text_color, weight='bold', zorder=5)
    else:
        ax.text(x + w/2, y + h*0.80, stereotype, fontsize=7.5, ha='center', va='center', color="#475569", style='italic', weight='bold', zorder=5)
        for idx, line in enumerate(lines):
            ax.text(x + w/2, y + h*(0.55 - idx*0.18), line, fontsize=8.2, ha='center', va='center', color=text_color, weight='bold', zorder=5)

def draw_port(ax, x, y, size=0.22, color="#1D4E89"):
    ax.add_patch(Rectangle((x - size/2, y - size/2), size, size, facecolor="#FFFFFF", edgecolor=color, linewidth=1.2, zorder=6))

def draw_provided_interface(ax, start_x, start_y, end_x, end_y, label, label_pos="top", color="#0284C7"):
    ax.plot([start_x, end_x], [start_y, end_y], color=color, linewidth=1.4, zorder=3)
    r = 0.18
    circle = Circle((end_x, end_y), r, facecolor="#FFFFFF", edgecolor=color, linewidth=1.6, zorder=5)
    ax.add_patch(circle)
    offset_y = 0.28 if label_pos == "top" else -0.32
    ax.text(end_x, end_y + offset_y, label, fontsize=7.8, ha='center', va='center', color="#0369A1", weight='bold', zorder=6)

def draw_required_interface(ax, start_x, start_y, end_x, end_y, angle_deg, label, label_pos="top", color="#DC2626"):
    ax.plot([start_x, end_x], [start_y, end_y], color=color, linewidth=1.3, linestyle='--', zorder=3)
    arc = Arc((end_x, end_y), 0.44, 0.44, angle=angle_deg, theta1=-90, theta2=90, color=color, linewidth=1.8, zorder=5)
    ax.add_patch(arc)
    offset_y = 0.28 if label_pos == "top" else -0.32
    ax.text(end_x, end_y + offset_y, label, fontsize=7.8, ha='center', va='center', color="#B91C1C", weight='bold', zorder=6)

def generate_uml_component_diagram(output_path="uml_component_diagram.png"):
    fig, ax = plt.subplots(figsize=(20, 13.5), dpi=300)
    ax.set_xlim(0, 27)
    ax.set_ylim(0, 17)
    ax.axis('off')
    
    # Canvas Background
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    
    # Diagram Title Header
    ax.text(13.5, 16.4, "UML 2.0 COMPONENT MODEL & SUBSYSTEM DECOMPOSITION", fontsize=15, weight='bold', ha='center', va='center', color='#0F2942')
    ax.text(13.5, 16.0, "System: Group Travel Expense Simplification Engine | Primary Domain: Retail, E-Commerce & Finance",
            fontsize=10.5, ha='center', va='center', color='#475569')

    # Subsystem Boundaries (Package/Subsystem boxes)
    # 1. Client / Presentation Layer
    ax.add_patch(FancyBboxPatch((0.8, 12.8), 25.4, 2.4, boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor="#F1F5F9", edgecolor="#CBD5E1", linewidth=1.2, linestyle=':', zorder=1))
    ax.text(1.2, 14.9, "«subsystem» Client & Presentation Tier", fontsize=10, weight='bold', color="#334155")

    # 2. API Gateway & Security Layer
    ax.add_patch(FancyBboxPatch((0.8, 9.6), 25.4, 2.6, boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor="#FAF5FF", edgecolor="#D8B4FE", linewidth=1.2, linestyle=':', zorder=1))
    ax.text(1.2, 11.9, "«subsystem» API Gateway & Edge Security Tier", fontsize=10, weight='bold', color="#6B21A8")

    # 3. Core Application & Domain Services Layer
    ax.add_patch(FancyBboxPatch((0.8, 4.4), 17.8, 4.6, boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor="#F0FDF4", edgecolor="#86EFAC", linewidth=1.3, linestyle='--', zorder=1))
    ax.text(1.2, 8.7, "«subsystem» Core Financial & Trip Domain Services Tier", fontsize=10, weight='bold', color="#166534")

    # 4. Algorithmic Debt Minimization Engine (Highlighted Core)
    ax.add_patch(FancyBboxPatch((19.0, 4.4), 7.2, 4.6, boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor="#FEF9C3", edgecolor="#FACC15", linewidth=1.5, linestyle='-', zorder=1))
    ax.text(19.4, 8.7, "«subsystem» Algorithmic Optimization Tier", fontsize=10, weight='bold', color="#854D0E")

    # 5. External Third-Party Services Subsystem
    ax.add_patch(FancyBboxPatch((0.8, 0.8), 15.0, 3.1, boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor="#FFF1F2", edgecolor="#FECDD3", linewidth=1.2, linestyle=':', zorder=1))
    ax.text(1.2, 3.6, "«subsystem» External Integrations & Cloud Infrastructure", fontsize=10, weight='bold', color="#9F1239")

    # 6. Persistence & Storage Subsystem
    ax.add_patch(FancyBboxPatch((16.2, 0.8), 10.0, 3.1, boxstyle="round,pad=0.1,rounding_size=0.2",
                                facecolor="#F8FAFC", edgecolor="#CBD5E1", linewidth=1.2, linestyle=':', zorder=1))
    ax.text(16.6, 3.6, "«subsystem» Persistence & Cache Tier", fontsize=10, weight='bold', color="#334155")

    # --- COMPONENTS ---
    # Client Components
    draw_component(ax, 2.5, 13.1, 4.6, 1.5, "Traveler Web App\n(React SPA)", "«component»", "#E0F2FE", "#0284C7", "#0369A1")
    draw_component(ax, 8.6, 13.1, 4.6, 1.5, "Traveler Mobile App\n(iOS / Android Native)", "«component»", "#E0F2FE", "#0284C7", "#0369A1")
    draw_component(ax, 15.0, 13.1, 4.6, 1.5, "Trip Admin Portal\n(Management Console)", "«component»", "#E0F2FE", "#0284C7", "#0369A1")

    # Target Actors
    ax.text(1.4, 13.85, "«actor»\nGroup Traveler", fontsize=8.2, weight='bold', ha='center', color="#0F172A")
    ax.plot([2.1, 2.5], [13.85, 13.85], color="#64748B", linewidth=1.3)
    ax.text(21.2, 13.85, "«actor»\nTrip Admin", fontsize=8.2, weight='bold', ha='center', color="#0F172A")
    ax.plot([19.6, 20.3], [13.85, 13.85], color="#64748B", linewidth=1.3)

    # API Gateway & Security Components
    draw_component(ax, 2.5, 10.0, 5.2, 1.6, "API Gateway &\nReverse Proxy", "«component»", "#EDE9FE", "#7C3AED", "#5B21B6")
    draw_component(ax, 9.8, 10.0, 5.0, 1.6, "Auth & Session\nManager Component", "«component»", "#EDE9FE", "#7C3AED", "#5B21B6")
    draw_component(ax, 16.8, 10.0, 5.2, 1.6, "Rate Limiter &\nAudit Logger", "«component»", "#EDE9FE", "#7C3AED", "#5B21B6")

    # Core Domain Components
    draw_component(ax, 1.2, 6.4, 4.4, 1.7, "Trip Management\nComponent", "«component»", "#DCFCE7", "#16A34A", "#15803D")
    draw_component(ax, 6.4, 6.4, 4.6, 1.7, "Expense & Receipt\nManager Component", "«component»", "#DCFCE7", "#16A34A", "#15803D")
    draw_component(ax, 12.0, 6.4, 4.4, 1.7, "Split Calculation\nRule Engine", "«component»", "#DCFCE7", "#16A34A", "#15803D")

    draw_component(ax, 1.2, 4.6, 4.4, 1.5, "Currency Conversion\nService", "«component»", "#DCFCE7", "#16A34A", "#15803D")
    draw_component(ax, 6.4, 4.6, 4.6, 1.5, "Settlement & Payment\nReconciliation Component", "«component»", "#DCFCE7", "#16A34A", "#15803D")
    draw_component(ax, 12.0, 4.6, 4.4, 1.5, "Event Notification\nDispatcher Component", "«component»", "#DCFCE7", "#16A34A", "#15803D")

    # Algorithmic Debt Minimization Engine (Core)
    draw_component(ax, 19.4, 4.7, 6.4, 3.4, "Debt Simplification &\nOptimization Engine\n(Greedy Min-Cash-Flow /\nBipartite Graph Reducer)",
                   "«component»\n[Core Algorithmic Unit]", "#FEF08A", "#CA8A04", "#713F12")

    # External APIs
    draw_component(ax, 1.2, 1.1, 4.2, 1.4, "Payment Gateway API\n(UPI / Stripe / NetBanking)", "«external system»", "#FEE2E2", "#DC2626", "#991B1B")
    draw_component(ax, 6.0, 1.1, 4.2, 1.4, "Forex Exchange Rates API\n(OpenExchangeRates)", "«external system»", "#FEE2E2", "#DC2626", "#991B1B")
    draw_component(ax, 10.8, 1.1, 4.4, 1.4, "Receipt Storage & Push\n(AWS S3 / Firebase FCM)", "«external system»", "#FEE2E2", "#DC2626", "#991B1B")

    # Persistence / DBs
    draw_component(ax, 16.6, 1.1, 4.2, 1.4, "PostgreSQL Ledger\n(ACID Relational DB)", "«database»", "#E2E8F0", "#334155", "#0F172A")
    draw_component(ax, 21.4, 1.1, 4.2, 1.4, "Redis Cache & Broker\n(In-Memory Store)", "«cache / broker»", "#E2E8F0", "#334155", "#0F172A")

    # --- INTERFACES & CONNECTORS ---
    # Client to API Gateway
    draw_port(ax, 5.1, 11.6)
    draw_port(ax, 5.1, 13.1)
    ax.plot([5.1, 5.1], [13.1, 11.6], color="#0284C7", linewidth=1.5)
    draw_provided_interface(ax, 5.1, 11.6, 5.1, 12.35, "IClientREST / WSS", "top")

    # Mobile App to Gateway
    draw_port(ax, 10.9, 13.1)
    ax.plot([10.9, 5.1], [13.1, 12.35], color="#0284C7", linewidth=1.2, linestyle=':')

    # Gateway to Core Services
    ax.plot([5.1, 5.1], [10.0, 8.4], color="#7C3AED", linewidth=1.3)
    ax.plot([3.4, 14.2], [8.4, 8.4], color="#7C3AED", linewidth=1.3)
    
    draw_provided_interface(ax, 3.4, 8.1, 3.4, 8.4, "ITripService", "top")
    draw_provided_interface(ax, 8.7, 8.1, 8.7, 8.4, "IExpenseService", "top")
    draw_provided_interface(ax, 14.2, 8.1, 14.2, 8.4, "ISplitService", "top")

    # Auth interface
    draw_provided_interface(ax, 9.8, 10.8, 8.5, 10.8, "IAuthService", "top")
    draw_required_interface(ax, 7.7, 10.8, 8.4, 10.8, 180, "", "top")

    # Intra-service connectors:
    # Expense -> SplitService
    ax.plot([11.0, 12.0], [7.25, 7.25], color="#16A34A", linewidth=1.4)
    draw_port(ax, 11.0, 7.25)
    draw_port(ax, 12.0, 7.25)
    ax.text(11.5, 7.45, "ISplitService", fontsize=7.5, ha='center', color="#15803D", weight='bold')

    # Expense -> CurrencyService
    ax.plot([3.4, 6.4], [5.35, 5.35], color="#475569", linewidth=1.3, linestyle='--')
    ax.text(4.9, 5.55, "ICurrencyService", fontsize=7.5, ha='center', color="#334155", weight='bold')

    # Core Engine Connections
    draw_port(ax, 19.4, 6.8)
    draw_provided_interface(ax, 19.4, 6.8, 17.5, 6.8, "ISimplificationEngine\n(getMinTransactions, getNetBalances)", "top")
    # Expense & Settlement depend on Simplification Engine
    draw_required_interface(ax, 11.0, 6.8, 17.3, 6.8, 0, "", "top")
    draw_required_interface(ax, 11.0, 5.35, 17.3, 5.35, 0, "ISettlementService", "bottom")
    ax.plot([17.3, 17.3], [5.35, 6.8], color="#DC2626", linewidth=1.2, linestyle='--')

    # Settlement -> Payment Gateway API
    draw_port(ax, 8.7, 4.6)
    ax.plot([8.7, 8.7, 3.3, 3.3], [4.6, 3.1, 3.1, 2.5], color="#DC2626", linewidth=1.3, linestyle='--')
    draw_required_interface(ax, 3.3, 2.7, 3.3, 2.5, 270, "IPaymentGateway", "top")

    # Currency Service -> Live Exchange Rates API
    draw_port(ax, 3.4, 4.6)
    ax.plot([3.4, 3.4, 8.1, 8.1], [4.6, 2.9, 2.9, 2.5], color="#DC2626", linewidth=1.3, linestyle='--')
    draw_required_interface(ax, 8.1, 2.7, 8.1, 2.5, 270, "IForexRateAPI", "top")

    # Notification & Storage Dispatch
    draw_port(ax, 14.2, 4.6)
    ax.plot([14.2, 14.2, 13.0, 13.0], [4.6, 2.9, 2.9, 2.5], color="#7C3AED", linewidth=1.3, linestyle='--')
    draw_required_interface(ax, 13.0, 2.7, 13.0, 2.5, 270, "IStorageAndPushAPI", "top")

    # Persistence Connections (to PostgreSQL & Redis)
    ax.plot([18.7, 18.7], [4.4, 2.5], color="#334155", linewidth=1.4)
    draw_provided_interface(ax, 18.7, 2.5, 18.7, 3.0, "ILedgerPersistence (ACID)", "top")
    
    ax.plot([23.5, 23.5], [4.4, 2.5], color="#334155", linewidth=1.4)
    draw_provided_interface(ax, 23.5, 2.5, 23.5, 3.0, "ICachePersistence", "top")

    # --- UML NOTATION KEY (Top Banner) ---
    leg_x, leg_y, leg_w, leg_h = 0.8, 15.3, 25.4, 0.55
    ax.add_patch(Rectangle((leg_x, leg_y), leg_w, leg_h, facecolor="#FFFFFF", edgecolor="#CBD5E1", linewidth=1.0, zorder=3))
    
    ax.text(leg_x + 0.3, leg_y + 0.28, "UML 2.0 NOTATION KEY:", fontsize=8.2, weight='bold', color="#0F172A", va='center')
    
    # Component icon sample
    ax.add_patch(Rectangle((leg_x + 3.8, leg_y + 0.14), 0.45, 0.28, facecolor="#EBF3FA", edgecolor="#1D4E89", linewidth=1.0, zorder=4))
    ax.text(leg_x + 4.4, leg_y + 0.28, "Component", fontsize=7.8, color="#1E293B", va='center')
    
    # Provided interface sample (lollipop)
    ax.plot([leg_x + 6.8, leg_x + 7.4], [leg_y + 0.28, leg_y + 0.28], color="#0284C7", linewidth=1.3)
    ax.add_patch(Circle((leg_x + 7.4, leg_y + 0.28), 0.09, facecolor="#FFFFFF", edgecolor="#0284C7", linewidth=1.3))
    ax.text(leg_x + 7.7, leg_y + 0.28, "Provided Interface (Lollipop)", fontsize=7.8, color="#1E293B", va='center')

    # Required interface sample (socket)
    ax.plot([leg_x + 12.2, leg_x + 12.7], [leg_y + 0.28, leg_y + 0.28], color="#DC2626", linewidth=1.3, linestyle='--')
    ax.add_patch(Arc((leg_x + 12.7, leg_y + 0.28), 0.2, 0.2, angle=0, theta1=-90, theta2=90, color="#DC2626", linewidth=1.5))
    ax.text(leg_x + 13.0, leg_y + 0.28, "Required Interface (Socket)", fontsize=7.8, color="#1E293B", va='center')

    # Port sample
    ax.add_patch(Rectangle((leg_x + 17.4, leg_y + 0.18), 0.16, 0.16, facecolor="#FFFFFF", edgecolor="#1D4E89", linewidth=1.2))
    ax.text(leg_x + 17.8, leg_y + 0.28, "Port", fontsize=7.8, color="#1E293B", va='center')

    # Assembly Connector
    ax.plot([leg_x + 19.5, leg_x + 19.9], [leg_y + 0.28, leg_y + 0.28], color="#0284C7", linewidth=1.2)
    ax.add_patch(Circle((leg_x + 19.9, leg_y + 0.28), 0.08, facecolor="#FFFFFF", edgecolor="#0284C7", linewidth=1.2))
    ax.add_patch(Arc((leg_x + 19.9, leg_y + 0.28), 0.18, 0.18, angle=0, theta1=-90, theta2=90, color="#DC2626", linewidth=1.4))
    ax.plot([leg_x + 19.9, leg_x + 20.3], [leg_y + 0.28, leg_y + 0.28], color="#DC2626", linewidth=1.2, linestyle='--')
    ax.text(leg_x + 20.5, leg_y + 0.28, "Assembly Connector", fontsize=7.8, color="#1E293B", va='center')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"UML Component Diagram successfully generated at: {output_path}")

if __name__ == "__main__":
    generate_uml_component_diagram()
