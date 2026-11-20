"""
Professional PDF Deliverable Generator for Lab 3
Lab Title: Lab 3 – Component Modelling & Architectural Pattern Selection
System: Group Travel Expense Simplification Engine
Domain: Retail, E-Commerce & Finance
Student: Sakthevel Saravanan (PES1UG24CS405)
Course: UE23CS341A Software Engineering
"""
import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and render total page count 'Page X of Y'
    along with running headers and footers.
    """
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#475569"))
        
        # Header (Pages 2+)
        if self._pageNumber > 1:
            self.drawString(54, 804, "Lab 3 – Component Modelling & Architectural Pattern Selection")
            self.setFont("Helvetica", 8)
            self.drawRightString(541, 804, f"Page {self._pageNumber} of {page_count}")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.6)
            self.line(54, 798, 541, 798)

        # Footer (All Pages)
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.6)
        self.line(54, 44, 541, 44)
        
        self.setFont("Helvetica", 8)
        self.drawString(54, 32, "UE23CS341A: Software Engineering | Department of CSE, PES University")
        self.drawRightString(541, 32, "Sakthevel Saravanan | PES1UG24CS405")
        self.restoreState()


def build_lab3_pdf(filename="Lab_3_Component_Modelling_Architectural_Pattern_Selection_Sakthevel_Saravanan.pdf"):
    # Target 6-page structured document
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=50,
        rightMargin=50,
        topMargin=48,
        bottomMargin=48
    )

    styles = getSampleStyleSheet()

    PRIMARY = colors.HexColor("#0F2942")     # Deep Navy
    SECONDARY = colors.HexColor("#1D4E89")   # Executive Blue
    TEXT_DARK = colors.HexColor("#1E293B")   # Slate 800
    TEXT_MUTED = colors.HexColor("#64748B")  # Slate 500

    style_cover_pre = ParagraphStyle(
        'CoverPre',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=SECONDARY,
        spaceAfter=2
    )

    style_cover_title = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=PRIMARY,
        spaceAfter=4
    )

    style_cover_sub = ParagraphStyle(
        'CoverSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=TEXT_MUTED,
        spaceAfter=8
    )

    style_h1 = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=PRIMARY,
        spaceBefore=7,
        spaceAfter=4,
        keepWithNext=True
    )

    style_h2 = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=SECONDARY,
        spaceBefore=5,
        spaceAfter=3,
        keepWithNext=True
    )

    style_body = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.2,
        textColor=TEXT_DARK,
        spaceAfter=4
    )

    style_bullet = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.6,
        textColor=TEXT_DARK,
        leftIndent=10,
        spaceAfter=2
    )

    style_table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.8,
        leading=10,
        textColor=colors.white,
        alignment=0
    )

    style_table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.4,
        leading=9.6,
        textColor=TEXT_DARK
    )

    style_table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.4,
        leading=9.6,
        textColor=PRIMARY
    )

    style_code = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=6.8,
        leading=8.5,
        textColor=colors.HexColor("#0F172A")
    )

    story = []

    # ================= PAGE 1: TITLE BLOCK, METADATA & EXECUTIVE SUMMARY =================
    story.append(Paragraph("LAB 3 DELIVERABLE REPORT", style_cover_pre))
    story.append(Paragraph("Component Modelling & Architectural Pattern Selection", style_cover_title))
    story.append(Paragraph("System Architecture Design, Component Decomposition, Interface Specifications & Pattern Evaluation", style_cover_sub))
    story.append(HRFlowable(width="100%", thickness=1.2, color=SECONDARY, spaceBefore=0, spaceAfter=8))

    metadata_data = [
        [Paragraph("<b>Student Name:</b>", style_table_cell_bold), Paragraph("Sakthevel Saravanan", style_table_cell),
         Paragraph("<b>SRN:</b>", style_table_cell_bold), Paragraph("PES1UG24CS405", style_table_cell)],
        [Paragraph("<b>Course:</b>", style_table_cell_bold), Paragraph("UE23CS341A: Software Engineering", style_table_cell),
         Paragraph("<b>Semester / Term:</b>", style_table_cell_bold), Paragraph("B.Tech CSE - 5th Semester", style_table_cell)],
        [Paragraph("<b>Project Title:</b>", style_table_cell_bold), Paragraph("Group Travel Expense Simplification Engine", style_table_cell),
         Paragraph("<b>Primary Domain:</b>", style_table_cell_bold), Paragraph("Retail, E-Commerce & Finance", style_table_cell)],
        [Paragraph("<b>Target Actors:</b>", style_table_cell_bold), Paragraph("Group Traveler (User), Trip Admin (Organizer)", style_table_cell),
         Paragraph("<b>Supporting Actors:</b>", style_table_cell_bold), Paragraph("Payment Gateway (UPI/Stripe), Forex Rate API", style_table_cell)]
    ]
    t_meta = Table(metadata_data, colWidths=[80, 168, 80, 167])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('PADDING', (0,0), (-1,-1), 3.5),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 6))

    story.append(Paragraph("1. Executive Summary & Problem Context", style_h1))
    story.append(Paragraph(
        "<b>Project Background:</b> In group travel scenarios, shared expenses (accommodations, transport, dining, group passes) "
        "are incurred across multiple participants using different currencies and payment methods. At trip conclusion, computing who owes "
        "whom results in mutual cross-payments, mathematical errors, and payment friction.",
        style_body
    ))
    story.append(Paragraph(
        "<b>Core Value Proposition:</b> The <i>Group Travel Expense Simplification Engine</i> provides an automated financial platform that: "
        "(1) captures multi-currency group expenses with flexible split models (equal, exact, percentage, shares), (2) standardizes costs into a "
        "base currency, (3) computes real-time net balances (Paid - Owed) for all members, and (4) uses a Greedy Minimum-Cash-Flow graph algorithm "
        "to reduce $O(N^2)$ cross-debts down to at most $N-1$ settlement transfers via integrated payment gateways (UPI, Stripe).",
        style_body
    ))
    story.append(Paragraph(
        "<b>Lab 3 Focus:</b> Decomposing system capabilities into high-cohesion UML components, establishing explicit provided/required interfaces, "
        "evaluating alternative architectural patterns, and rigorously justifying the chosen hybrid architecture.",
        style_body
    ))

    story.append(Paragraph("2. System Scope & Quality Attributes (Tracing to Lab 1)", style_h1))
    scope_data = [
        [Paragraph("Category", style_table_header), Paragraph("Requirement & Scope Description", style_table_header), Paragraph("Lab 1 Mapping / NFR", style_table_header)],
        [Paragraph("<b>Identity & Security</b>", style_table_cell), Paragraph("Token-based authentication, user profile management, payment handle binding.", style_table_cell), Paragraph("UC-01 Login", style_table_cell)],
        [Paragraph("<b>Trip Workspace</b>", style_table_cell), Paragraph("Trip creation, member invitation, base currency configuration, trip closure.", style_table_cell), Paragraph("UC-02 Manage Trip", style_table_cell)],
        [Paragraph("<b>Expense Logging</b>", style_table_cell), Paragraph("Multi-currency expenditure logging, payer tagging, digital receipt storage.", style_table_cell), Paragraph("UC-03 Record Expense", style_table_cell)],
        [Paragraph("<b>Split Rule Engine</b>", style_table_cell), Paragraph("Equal, unequal, percentage, and share splits with strict zero-sum validation.", style_table_cell), Paragraph("UC-04 Split Expense", style_table_cell)],
        [Paragraph("<b>Debt Simplification</b>", style_table_cell), Paragraph("Net balance calculations and algorithmic debt graph transaction minimization.", style_table_cell), Paragraph("UC-05 View Balance", style_table_cell)],
        [Paragraph("<b>Settlement Gateway</b>", style_table_cell), Paragraph("Direct and gateway payment execution (UPI/Stripe), webhook reconciliation.", style_table_cell), Paragraph("UC-06 Settle Expenses", style_table_cell)],
        [Paragraph("<b>Event Notifications</b>", style_table_cell), Paragraph("Asynchronous push, SMS, and email alerts for expense changes and settlements.", style_table_cell), Paragraph("UC-07 Notification", style_table_cell)],
        [Paragraph("<b>Precision & ACID</b>", style_table_cell), Paragraph("4-decimal fixed-point math; atomic transactional consistency for ledger.", style_table_cell), Paragraph("NFR-01/02 Precision & ACID", style_table_cell)],
        [Paragraph("<b>Fault Isolation</b>", style_table_cell), Paragraph("External gateway/forex latency isolated via circuit breakers and queues.", style_table_cell), Paragraph("NFR-03 Fault Resilience", style_table_cell)]
    ]
    t_scope = Table(scope_data, colWidths=[95, 290, 110])
    t_scope.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 2.8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_scope)

    # ================= PAGE 2: COMPONENT DECOMPOSITION =================
    story.append(PageBreak())
    story.append(Paragraph("3. Component Decomposition & Structural Modelling", style_h1))
    story.append(Paragraph(
        "Applying the architectural principles of <b>High Cohesion</b>, <b>Loose Coupling</b>, and <b>Information Hiding</b>, "
        "the system is decomposed into 9 core autonomous components organized across structural layers:",
        style_body
    ))

    comp_specs = [
        [Paragraph("Component Name", style_table_header), Paragraph("Provided Interface (Lollipop)", style_table_header), Paragraph("Required Interface (Socket)", style_table_header), Paragraph("Core Responsibilities & Implementation Details", style_table_header)],
        
        [Paragraph("<b>API Gateway & Edge Router</b><br/>«component»", style_table_cell_bold),
         Paragraph("<code>IClientREST<br/>IWebSocketStream</code>", style_code),
         Paragraph("<code>IAuthService<br/>ITripService<br/>IExpenseService<br/>ISettlementService</code>", style_code),
         Paragraph("Single point of entry for clients. Handles SSL termination, JWT authentication verification, request rate-limiting, CORS handling, and intelligent reverse proxy routing.", style_table_cell)],

        [Paragraph("<b>Auth & Identity Manager</b><br/>«component»", style_table_cell_bold),
         Paragraph("<code>IAuthService</code><br/>• login()<br/>• registerUser()<br/>• verifyToken()", style_code),
         Paragraph("<code>IUserPersistence<br/>ITokenStore</code>", style_code),
         Paragraph("Manages user identity lifecycle, Argon2id password hashing, JWT session tokens, traveler profiles, and payment handles (UPI IDs, bank details).", style_table_cell)],

        [Paragraph("<b>Trip Management Service</b><br/>«component»", style_table_cell_bold),
         Paragraph("<code>ITripService</code><br/>• createTrip()<br/>• addMember()<br/>• setBaseCurrency()", style_code),
         Paragraph("<code>ITripPersistence<br/>IUserProfileService<br/>INotificationService</code>", style_code),
         Paragraph("Encapsulates trip entity lifecycle, admin role privileges, traveler group rosters, base currency settings, and historical trip archival.", style_table_cell)],

        [Paragraph("<b>Expense & Receipt Manager</b><br/>«component»", style_table_cell_bold),
         Paragraph("<code>IExpenseService</code><br/>• recordExpense()<br/>• updateExpense()<br/>• getTripExpenses()", style_code),
         Paragraph("<code>IExpensePersistence<br/>ISplitService<br/>ICurrencyService<br/>IStorageService</code>", style_code),
         Paragraph("Central business facade for expenses. Handles receipt image uploading, invokes currency conversion, validates participants, and writes ledger entries.", style_table_cell)],

        [Paragraph("<b>Split Calculation Rule Engine</b><br/>«component»", style_table_cell_bold),
         Paragraph("<code>ISplitService</code><br/>• splitEqually()<br/>• splitByPercentage()<br/>• splitByExact()", style_code),
         Paragraph("<i>None (Pure Domain Engine)</i>", style_table_cell),
         Paragraph("Stateless, highly cohesive mathematical rule engine. Calculates fractional liability allocations; verifies that sum of shares equals total amount.", style_table_cell)],

        [Paragraph("<b>Currency Conversion Service</b><br/>«component»", style_table_cell_bold),
         Paragraph("<code>ICurrencyService</code><br/>• convertAmount()<br/>• getRates()", style_code),
         Paragraph("<code>IForexRateAPI<br/>IRateCachePersistence</code>", style_code),
         Paragraph("Normalizes multi-currency spending to base trip currency. Fetches live forex rates, leveraging Redis cache with offline fallback.", style_table_cell)],

        [Paragraph("<b>Debt Simplification Engine</b><br/>«component»<br/><i>[Algorithmic Core]</i>", style_table_cell_bold),
         Paragraph("<code>ISimplificationEngine</code><br/>• computeNetBalances()<br/>• getMinTransactions()", style_code),
         Paragraph("<code>IExpensePersistence<br/>ITripPersistence</code>", style_code),
         Paragraph("<b>Algorithmic Heart:</b> Computes net balances vector. Partitions members into debtors and creditors; executes Greedy Min-Cash-Flow matching to minimize transactions.", style_table_cell)],

        [Paragraph("<b>Settlement & Reconciliation</b><br/>«component»", style_table_cell_bold),
         Paragraph("<code>ISettlementService</code><br/>• initiatePayment()<br/>• confirmSettlement()", style_code),
         Paragraph("<code>IPaymentGateway<br/>ISimplificationEngine<br/>ILedgerPersistence</code>", style_code),
         Paragraph("Facilitates debt settlement. Generates dynamic UPI intent links, processes payment gateway webhooks, and reconciles settled balances in the ledger.", style_table_cell)],

        [Paragraph("<b>Notification Dispatcher</b><br/>«component»", style_table_cell_bold),
         Paragraph("<code>INotificationService</code><br/>• sendExpenseAlert()<br/>• sendSettlementPrompt()", style_code),
         Paragraph("<code>IStorageAndPushAPI<br/>IMessageBroker</code>", style_code),
         Paragraph("Asynchronous message dispatcher. Consumes domain events from Kafka/Redis and broadcasts mobile push alerts (FCM), SMS, and email summaries.", style_table_cell)],

        [Paragraph("<b>Persistence & Storage Tier</b><br/>«database / cache»", style_table_cell_bold),
         Paragraph("<code>ILedgerPersistence<br/>ICachePersistence</code>", style_code),
         Paragraph("<i>Host Storage / File System</i>", style_table_cell),
         Paragraph("PostgreSQL relational database guaranteeing ACID properties for financial audit trails, coupled with Redis for session states and rapid caching.", style_table_cell)]
    ]

    t_comp = Table(comp_specs, colWidths=[90, 115, 105, 185])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 2.8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_comp)

    # ================= PAGE 3: FORMAL UML COMPONENT DIAGRAM =================
    story.append(PageBreak())
    story.append(Paragraph("4. UML 2.0 Component Diagram", style_h1))
    story.append(Paragraph(
        "The following diagram presents the formal structural component model of the <b>Group Travel Expense Simplification Engine</b>, "
        "depicting component boundaries, provided interfaces (lollipops), required interfaces (sockets), ports, and external infrastructure:",
        style_body
    ))

    diagram_path = "uml_component_diagram.png"
    if os.path.exists(diagram_path):
        story.append(Image(diagram_path, width=6.8*inch, height=4.2*inch))
    else:
        story.append(Paragraph("<i>[Diagram file uml_component_diagram.png not found]</i>", style_body))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Detailed Notational Elements & Subsystem Architectural Layers:</b>", style_h2))
    story.append(Paragraph(
        "• <b>Lollipop Notation (Circle):</b> Represents a <i>Provided Interface</i> exposing operations that a component implements and offers to other components (e.g., <code>IExpenseService</code> provided by Expense Manager).<br/>"
        "• <b>Socket Notation (Semi-Circle Arc):</b> Represents a <i>Required Interface</i> denoting an operational dependency that the component requires to execute its responsibilities (e.g., Expense Manager requiring <code>ISplitService</code>).<br/>"
        "• <b>Assembly Connector:</b> Formed by a lollipop fitting inside a socket, representing direct interface binding and loose structural coupling between autonomous components.<br/>"
        "• <b>Ports (Small Squares):</b> Explicit interaction endpoints through which external messages and network protocols (REST, WSS, AMQP) penetrate component encapsulation boundaries.<br/>"
        "• <b>Subsystem Boundaries:</b> The system is segmented into 6 cohesive subsystems: (1) Client Tier, (2) API Gateway Tier, (3) Core Domain Services Tier, (4) Algorithmic Optimization Tier, (5) External Cloud Integrations, and (6) Persistence Tier.",
        style_bullet
    ))

    # ================= PAGE 4: ARCHITECTURAL PATTERN SELECTION & MATRIX =================
    story.append(PageBreak())
    story.append(Paragraph("5. Architectural Pattern Selection & Justification", style_h1))
    story.append(Paragraph(
        "The selection of an architectural pattern provides the structural schema and design constraints that govern component interactions, "
        "scalability, and resilience. Below, candidate patterns are rigorously evaluated against group travel finance requirements.",
        style_body
    ))

    story.append(Paragraph("5.1 Comparative Evaluation of Candidate Architectural Styles", style_h2))
    
    pattern_eval_data = [
        [Paragraph("Architectural Pattern", style_table_header),
         Paragraph("Structural Description", style_table_header),
         Paragraph("Strengths in Context", style_table_header),
         Paragraph("Limitations / Rejection Rationale", style_table_header)],

        [Paragraph("<b>Monolithic Layered (N-Tier)</b>", style_table_cell_bold),
         Paragraph("Hierarchical layering: Presentation, Logic, Data Access in a single codebase.", style_table_cell),
         Paragraph("Simple deployment, straightforward database ACID transactions.", style_table_cell),
         Paragraph("<b>Rejected:</b> Compute-heavy debt minimization cannot scale independently from I/O; external API latency risks cascading crashes.", style_table_cell)],

        [Paragraph("<b>Model-View-Controller (MVC)</b>", style_table_cell_bold),
         Paragraph("Separates data Model, View presentation, and Controller user input logic.", style_table_cell),
         Paragraph("Effective for frontend UI interactions and traditional server-side rendering.", style_table_cell),
         Paragraph("<b>Rejected:</b> MVC is an application-level UI pattern, not a macro-architecture. Fails to decouple asynchronous payment webhooks or background graph solvers.", style_table_cell)],

        [Paragraph("<b>Pipes and Filters</b>", style_table_cell_bold),
         Paragraph("Stream of data transforms passing through sequential independent filters.", style_table_cell),
         Paragraph("Ideal for batch data processing (e.g. bulk receipt OCR parsing).", style_table_cell),
         Paragraph("<b>Rejected:</b> Ill-suited for interactive, bidirectional queries, concurrent user expense entries, and real-time ledger reconciliations.", style_table_cell)],

        [Paragraph("<b>Pure Microservices Architecture</b>", style_table_cell_bold),
         Paragraph("Fine-grained services, each owning private databases and domain models.", style_table_cell),
         Paragraph("High scalability, technology flexibility, independent deployments.", style_table_cell),
         Paragraph("<b>Partially Adopted:</b> High operational complexity; distributed 2PC/Sagas make financial ledger ACID guarantees overly fragile.", style_table_cell)],

        [Paragraph("<b>Selected: Modular Layered Microservices with Event-Driven Messaging</b>", style_table_cell_bold),
         Paragraph("<b>Hybrid Architecture:</b> Clear layering (Client, Gateway, Domain, Data) with autonomous domain services and an async Event Bus.", style_table_cell),
         Paragraph("<b>Optimal Fit:</b> Unifies strong ACID consistency on the ledger with horizontal scaling for debt minimization and resilient async integrations.", style_table_cell),
         Paragraph("<b>SELECTED:</b> Provides the ideal balance between transactional integrity, algorithmic compute scaling, and resilience against external gateway downtime.", style_table_cell)]
    ]

    t_patt = Table(pattern_eval_data, colWidths=[95, 115, 135, 150])
    t_patt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.HexColor("#F8FAFC")]),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#FEF3C7")),
        ('PADDING', (0,0), (-1,-1), 3.2),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_patt)
    story.append(Spacer(1, 4))

    story.append(Paragraph("5.2 Trade-off Evaluation Matrix Across Quality Attributes", style_h2))

    tradeoff_data = [
        [Paragraph("Quality Attribute / Dimension", style_table_header),
         Paragraph("Monolithic Layered", style_table_header),
         Paragraph("Pure Microservices", style_table_header),
         Paragraph("Pipes & Filters", style_table_header),
         Paragraph("Selected Hybrid Architecture", style_table_header)],
        
        [Paragraph("<b>Horizontal Scalability</b>", style_table_cell_bold), Paragraph("Low (Monolithic scaling)", style_table_cell), Paragraph("Very High", style_table_cell), Paragraph("Moderate", style_table_cell), Paragraph("<b>Very High (Targeted service scaling)</b>", style_table_cell)],
        [Paragraph("<b>Modularity & High Cohesion</b>", style_table_cell_bold), Paragraph("Moderate (Easy erosion)", style_table_cell), Paragraph("High", style_table_cell), Paragraph("High (Filter scope)", style_table_cell), Paragraph("<b>Exceptional (Explicit interfaces)</b>", style_table_cell)],
        [Paragraph("<b>Financial ACID Consistency</b>", style_table_cell_bold), Paragraph("Very High (Single DB)", style_table_cell), Paragraph("Low (Distributed Sagas)", style_table_cell), Paragraph("N/A", style_table_cell), Paragraph("<b>Very High (Unified Ledger DB)</b>", style_table_cell)],
        [Paragraph("<b>Fault Isolation & Resilience</b>", style_table_cell_bold), Paragraph("Low (Cascade crashes)", style_table_cell), Paragraph("High", style_table_cell), Paragraph("Moderate", style_table_cell), Paragraph("<b>High (Circuit Breakers & Queues)</b>", style_table_cell)],
        [Paragraph("<b>Debt Algorithm Performance</b>", style_table_cell_bold), Paragraph("Bound to web server CPU", style_table_cell), Paragraph("High (Dedicated workers)", style_table_cell), Paragraph("Moderate", style_table_cell), Paragraph("<b>Optimal (Stateless compute cluster)</b>", style_table_cell)],
        [Paragraph("<b>Development & Deploy Velocity</b>", style_table_cell_bold), Paragraph("High initially, degrades", style_table_cell), Paragraph("Moderate (DevOps cost)", style_table_cell), Paragraph("Moderate", style_table_cell), Paragraph("<b>High (Componentized modules)</b>", style_table_cell)],
        [Paragraph("<b>Operational Overhead</b>", style_table_cell_bold), Paragraph("Very Low", style_table_cell), Paragraph("Very High (K8s / Mesh)", style_table_cell), Paragraph("Moderate", style_table_cell), Paragraph("<b>Moderate (Managed cloud services)</b>", style_table_cell)]
    ]
    t_tradeoff = Table(tradeoff_data, colWidths=[125, 88, 90, 82, 110])
    t_tradeoff.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 2.8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_tradeoff)

    # ================= PAGE 5: DEEP ARCHITECTURAL JUSTIFICATION & CONTRACTS =================
    story.append(PageBreak())
    story.append(Paragraph("5.3 Detailed Architectural Justification Rationale", style_h1))
    story.append(Paragraph(
        "The selection of the <b>Modular Layered Microservices with Event-Driven Messaging</b> architecture is grounded in core software engineering tenets:",
        style_body
    ))

    story.append(Paragraph(
        "<b>1. High Cohesion & Single Responsibility Principle (SRP):</b><br/>"
        "Each component possesses a singular, tightly defined domain purpose. The <i>Debt Simplification Engine</i> contains purely mathematical "
        "graph minimization algorithms and zero UI, database, or notification logic. Conversely, the <i>Expense Manager</i> handles transaction "
        "intake without knowing how debts are simplified. High cohesion ensures that internal modifications (e.g., swapping from a greedy cash-flow "
        "algorithm to an optimal integer linear programming solver) are completely contained without ripple effects.",
        style_body
    ))

    story.append(Paragraph(
        "<b>2. Loose Coupling via Explicit Interfaces & Inversion of Control:</b><br/>"
        "Components interact strictly across well-defined abstraction boundaries (lollipops and sockets). Dependencies are inverted using dependency "
        "injection. The <i>Settlement Component</i> invokes <code>ISimplificationEngine</code> via an abstract interface, enabling mock implementations "
        "during unit testing and isolated deployment in production.",
        style_body
    ))

    story.append(Paragraph(
        "<b>3. Decoupling Compute-Bound vs. I/O-Bound Workloads:</b><br/>"
        "In travel expense systems, receipt image uploads and transaction inquiries are I/O intensive, whereas debt simplification for large travel "
        "contingents (e.g. 50+ members with hundreds of mutual receipts) is compute and memory intensive ($O(V \\log V)$ sorting and iterative bipartite flow). "
        "By isolating the <i>Simplification Engine</i> as an autonomous stateless component, it can scale horizontally on high-CPU worker nodes "
        "without consuming memory from web application servers.",
        style_body
    ))

    story.append(Paragraph(
        "<b>4. Fault Isolation & External Gateway Resilience:</b><br/>"
        "Travelers often record expenses in areas with unstable mobile connectivity or when external services (e.g. OpenExchangeRates or Stripe API) "
        "experience temporary outages. Using asynchronous message brokers (RabbitMQ/Kafka) and Circuit Breakers (Resilience4j pattern), expense "
        "recording succeeds locally and updates the PostgreSQL ledger immediately. Currency rate fetches and payment notification dispatches "
        "are queued asynchronously and retried with exponential backoff, preventing system-wide downtime.",
        style_body
    ))

    story.append(Paragraph(
        "<b>5. Financial Transactional Integrity (ACID vs. BASE Boundary):</b><br/>"
        "A critical flaw of pure microservices is data inconsistency across distributed databases. In this architecture, core financial entities "
        "(Users, Trips, Expenses, and Settlements) reside within a unified PostgreSQL relational schema guaranteeing ACID transactions and zero "
        "phantom balances. In contrast, non-critical event notifications, push alerts, and receipt images use eventual consistency (BASE), "
        "achieving the optimal equilibrium between correctness and performance.",
        style_body
    ))

    story.append(Paragraph("6. Interface Contracts & API Specifications", style_h1))
    story.append(Paragraph(
        "The following IDL specifications define the formal operational contracts exposed by the core component interfaces:",
        style_body
    ))

    contract_text = (
        "// 1. ISimplificationEngine (Core Algorithmic Optimization Contract)\n"
        "interface ISimplificationEngine {\n"
        "    computeNetBalances(tripId: UUID): Map<UserId, Decimal>;\n"
        "    minimizeTransactions(netBalances: Map<UserId, Decimal>): List<SimplifiedDebt>;\n"
        "    generateSettlementGraph(tripId: UUID): SettlementGraphDTO;\n"
        "}\n\n"
        "// 2. IExpenseService (Expense Ingestion & Orchestration Contract)\n"
        "interface IExpenseService {\n"
        "    recordExpense(dto: CreateExpenseDTO): ExpenseRecordResult;\n"
        "    updateExpense(expenseId: UUID, dto: UpdateExpenseDTO): ExpenseRecordResult;\n"
        "    getTripExpenseHistory(tripId: UUID, filter: ExpenseFilter): List<ExpenseDTO>;\n"
        "    uploadReceiptAttachment(expenseId: UUID, fileStream: Stream): ReceiptMetaDTO;\n"
        "}\n\n"
        "// 3. ISplitService (Pure Stateless Split Calculation Contract)\n"
        "interface ISplitService {\n"
        "    calculateEqualSplit(totalAmount: Decimal, participants: List<UserId>): Map<UserId, Decimal>;\n"
        "    calculatePercentageSplit(totalAmount: Decimal, shares: Map<UserId, Percentage>): Map<UserId, Decimal>;\n"
        "    calculateExactSplit(totalAmount: Decimal, exactShares: Map<UserId, Decimal>): ValidationResult;\n"
        "}\n\n"
        "// 4. ISettlementService (Payment Gateway & Financial Reconciliation Contract)\n"
        "interface ISettlementService {\n"
        "    initiatePeerPayment(debtId: UUID, method: PaymentMethod): PaymentSessionResponse;\n"
        "    handlePaymentWebhook(payload: WebhookPayload, signature: String): SettlementReceipt;\n"
        "    recordDirectCashSettlement(debtId: UUID, payerId: UserId, payeeId: UserId): SettlementReceipt;\n"
        "}"
    )

    t_code = Table([[Paragraph(f"<pre>{contract_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')}</pre>", style_code)]], colWidths=[495])
    t_code.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_code)

    # ================= PAGE 6: TRACEABILITY MATRIX & VERIFICATION =================
    story.append(PageBreak())
    story.append(Paragraph("7. Traceability Matrix: Mapping Lab 1 Use Cases to Components", style_h1))
    story.append(Paragraph(
        "To verify comprehensive system coverage and consistency across lab deliverables, the table below maps each use case "
        "defined in Lab 1 to its realizing components, exposed interfaces, and interactions:",
        style_body
    ))

    matrix_data = [
        [Paragraph("Use Case ID & Title", style_table_header),
         Paragraph("Primary Actor", style_table_header),
         Paragraph("Realizing Component(s)", style_table_header),
         Paragraph("Provided / Required Interface", style_table_header),
         Paragraph("Operational Mechanism", style_table_header)],

        [Paragraph("<b>UC-01 Login</b>", style_table_cell_bold),
         Paragraph("Group Traveler,<br/>Trip Admin", style_table_cell),
         Paragraph("Auth & Session Manager", style_table_cell),
         Paragraph("<code>IAuthService</code><br/><i>(Provided)</i>", style_code),
         Paragraph("Authenticates user credentials, validates MFA tokens, and issues signed JWT bearer tokens.", style_table_cell)],

        [Paragraph("<b>UC-02 Manage Trip</b>", style_table_cell_bold),
         Paragraph("Trip Admin", style_table_cell),
         Paragraph("Trip Management Component", style_table_cell),
         Paragraph("<code>ITripService</code><br/><i>(Provided)</i>", style_code),
         Paragraph("Creates trip workspace, configures base currency, invites member emails, assigns admin privileges.", style_table_cell)],

        [Paragraph("<b>UC-03 Record Expense</b>", style_table_cell_bold),
         Paragraph("Group Traveler", style_table_cell),
         Paragraph("Expense & Receipt Manager", style_table_cell),
         Paragraph("<code>IExpenseService</code><br/><i>(Provided)</i>", style_code),
         Paragraph("Ingests spending details, converts foreign currency, stores receipt image, writes to PostgreSQL ledger.", style_table_cell)],

        [Paragraph("<b>UC-04 Split Expense</b>", style_table_cell_bold),
         Paragraph("Group Traveler", style_table_cell),
         Paragraph("Split Calculation Rule Engine", style_table_cell),
         Paragraph("<code>ISplitService</code><br/><i>(Provided)</i>", style_code),
         Paragraph("Computes individual share amounts (equal, percentage, exact); validates that shares sum to amount.", style_table_cell)],

        [Paragraph("<b>UC-05 View Balance</b>", style_table_cell_bold),
         Paragraph("Group Traveler,<br/>Trip Admin", style_table_cell),
         Paragraph("Debt Simplification Engine", style_table_cell),
         Paragraph("<code>ISimplificationEngine</code><br/><i>(Provided)</i>", style_code),
         Paragraph("Computes net credit/debit balances, executes greedy cash-flow reduction, and returns minimum settlement plan.", style_table_cell)],

        [Paragraph("<b>UC-06 Settle Expenses</b>", style_table_cell_bold),
         Paragraph("Group Traveler,<br/>Payment Gateway", style_table_cell),
         Paragraph("Settlement & Payment Component", style_table_cell),
         Paragraph("<code>ISettlementService</code><br/><i>(Provided)</i>", style_code),
         Paragraph("Launches UPI / Stripe checkout intent, verifies webhook digital signatures, marks liabilities settled.", style_table_cell)],

        [Paragraph("<b>UC-07 Notification</b>", style_table_cell_bold),
         Paragraph("Group Traveler", style_table_cell),
         Paragraph("Event Notification Dispatcher", style_table_cell),
         Paragraph("<code>INotificationService</code><br/><i>(Provided)</i>", style_code),
         Paragraph("Listens to Kafka/Redis domain events and broadcasts mobile push alerts and email summaries to travelers.", style_table_cell)]
    ]

    t_matrix = Table(matrix_data, colWidths=[75, 70, 105, 105, 140])
    t_matrix.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 3.2),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_matrix)
    story.append(Spacer(1, 8))

    story.append(Paragraph("8. Conclusion & Submission Deliverable Checklist", style_h1))
    story.append(Paragraph(
        "<b>Summary of Architectural Outcomes:</b> The proposed component architecture structures the Group Travel Expense Simplification Engine "
        "into highly cohesive, loosely coupled units designed to satisfy rigorous financial consistency while delivering high performance for "
        "debt simplification algorithms. The selection of a <i>Modular Layered Microservices with Event-Driven Messaging</i> architecture ensures "
        "independent scalability for compute-heavy optimization, resilience against external API outages, and strict transactional integrity for financial audits.",
        style_body
    ))

    checklist_data = [
        [Paragraph("Required Lab 3 Deliverable Item", style_table_header), Paragraph("Compliance Status", style_table_header), Paragraph("Evidence / Section Reference", style_table_header)],
        [Paragraph("UML 2.0 Component Diagram with Provided & Required Interfaces", style_table_cell), Paragraph("<b>COMPLETED</b>", style_table_cell_bold), Paragraph("Section 4 (Embedded Vector Diagram with Lollipop/Socket Notation)", style_table_cell)],
        [Paragraph("Component Decomposition & Responsibilities", style_table_cell), Paragraph("<b>COMPLETED</b>", style_table_cell_bold), Paragraph("Section 3 (Comprehensive table covering all 9 subsystems & DBs)", style_table_cell)],
        [Paragraph("Architectural Pattern Evaluation & Trade-off Analysis", style_table_cell), Paragraph("<b>COMPLETED</b>", style_table_cell_bold), Paragraph("Section 5.1 & Section 5.2 (Comparative Matrix across 7 dimensions)", style_table_cell)],
        [Paragraph("Architectural Pattern Selection & Detailed Justification", style_table_cell), Paragraph("<b>COMPLETED</b>", style_table_cell_bold), Paragraph("Section 5.3 (High cohesion, coupling, compute decoupling, fault isolation)", style_table_cell)],
        [Paragraph("Interface Contracts & API Method Signatures", style_table_cell), Paragraph("<b>COMPLETED</b>", style_table_cell_bold), Paragraph("Section 6 (Complete TypeScript/IDL Interface Definitions)", style_table_cell)],
        [Paragraph("Traceability to Lab 1 Use Cases (UC-01 to UC-07)", style_table_cell), Paragraph("<b>COMPLETED</b>", style_table_cell_bold), Paragraph("Section 2 & Section 7 (Comprehensive Traceability Matrix)", style_table_cell)],
        [Paragraph("Formal PDF Deliverable Generation", style_table_cell), Paragraph("<b>COMPLETED</b>", style_table_cell_bold), Paragraph("Rendered via ReportLab with running headers/footers & metadata", style_table_cell)]
    ]

    t_check = Table(checklist_data, colWidths=[180, 95, 220])
    t_check.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), SECONDARY),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8FAFC")]),
        ('PADDING', (0,0), (-1,-1), 3.0),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_check)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully compiled Lab 3 PDF Deliverable: {filename}")

if __name__ == "__main__":
    build_lab3_pdf()
