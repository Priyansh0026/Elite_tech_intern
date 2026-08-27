import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_path = r"C:\Users\tanuj\OneDrive\Desktop\portfolio\PRIYANSH JAIN resume.pdf"

doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=30,
    rightMargin=30,
    topMargin=22,
    bottomMargin=22
)

styles = getSampleStyleSheet()

# Custom styles for 1-page fit
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    alignment=1, # Center
    textColor=colors.HexColor('#111111')
)

contact_style_line1 = ParagraphStyle(
    'ContactLine1',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=13,
    alignment=1, # Center
    textColor=colors.HexColor('#222222')
)

contact_style_line2 = ParagraphStyle(
    'ContactLine2',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=13,
    alignment=1, # Center
    textColor=colors.HexColor('#222222')
)

heading_style = ParagraphStyle(
    'SectionHeading',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=10.5,
    leading=13,
    textColor=colors.HexColor('#000000'),
    spaceBefore=5,
    spaceAfter=1
)

body_style = ParagraphStyle(
    'BodyText',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#111111')
)

bullet_style = ParagraphStyle(
    'BulletText',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8.3,
    leading=10.8,
    leftIndent=10,
    firstLineIndent=-6,
    textColor=colors.HexColor('#111111')
)

story = []

# Title
story.append(Paragraph("PRIYANSH JAIN", title_style))
story.append(Spacer(1, 2))

# Header Line 1: Moradabad, India | +91 9235596602 | Gmail
line1_text = (
    'Moradabad, India &nbsp;|&nbsp; +91 9235596602 &nbsp;|&nbsp; '
    '<a href="mailto:tjain0911@gmail.com" color="#111111"><u>Gmail</u></a>'
)
story.append(Paragraph(line1_text, contact_style_line1))

# Header Line 2: LinkedIn | GitHub | Portfolio
line2_text = (
    '<a href="https://www.linkedin.com/in/priyansh-jain-3a3665248" color="#111111"><u>LinkedIn</u></a> &nbsp;|&nbsp; '
    '<a href="https://github.com/Priyansh0026" color="#111111"><u>GitHub</u></a> &nbsp;|&nbsp; '
    '<a href="https://priyansh-jain.netlify.app" color="#111111"><u>Portfolio</u></a>'
)
story.append(Paragraph(line2_text, contact_style_line2))

story.append(Spacer(1, 2))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#111111'), spaceAfter=3, spaceBefore=2))

# Objective
story.append(Paragraph("OBJECTIVE", heading_style))
obj_text = (
    "Results-driven Computer Science student (2026) with a strong foundation in data engineering, statistical modeling, "
    "and data analytics. Proficient in performing exploratory data analysis (EDA) and visualizing complex datasets using "
    "Python (Pandas, NumPy, Matplotlib, Seaborn), SQL, and Power BI. Experienced in drawing logical, data-backed insights "
    "and building analytical workflows to support business decision-making. Seeking an entry level Data Analyst / Data Analytics role."
)
story.append(Paragraph(obj_text, body_style))

# Education
story.append(Paragraph("EDUCATION", heading_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#333333'), spaceAfter=2, spaceBefore=1))

edu_data = [
    [Paragraph("<b>Teerthanker Mahaveer University, Moradabad</b>", body_style), Paragraph("<b>2026</b>", ParagraphStyle('R1', parent=body_style, alignment=2))],
    [Paragraph("<i>B.Tech - Computer Science and Engineering</i>", body_style), Paragraph("<i>Moradabad, Uttar Pradesh</i>", ParagraphStyle('R2', parent=body_style, alignment=2))],
    [Paragraph("<b>Central Public School, Lalitpur</b>", body_style), Paragraph("<b>2024</b>", ParagraphStyle('R3', parent=body_style, alignment=2))],
    [Paragraph("<i>12th Standard</i>", body_style), Paragraph("<i>Lalitpur, Uttar Pradesh</i>", ParagraphStyle('R4', parent=body_style, alignment=2))],
]
t_edu = Table(edu_data, colWidths=[390, 160])
t_edu.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
story.append(t_edu)

# Internship
story.append(Paragraph("INTERNSHIP", heading_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#333333'), spaceAfter=2, spaceBefore=1))

intern_1 = [
    [Paragraph("<b>Sabudh Foundation (in Collaboration with STPI)</b>", body_style), Paragraph("<b>04/07/2026 – 17/08/2026</b>", ParagraphStyle('R5', parent=body_style, alignment=2))],
    [Paragraph("<i>Data Analytics Intern</i>", body_style), Paragraph("<i>Mohali, Punjab (Remote)</i>", ParagraphStyle('R6', parent=body_style, alignment=2))]
]
t_int1 = Table(intern_1, colWidths=[390, 160])
t_int1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
story.append(t_int1)

bullets_int1 = [
    "• Cleaned and preprocessed raw datasets using Python (Pandas, NumPy), resolving missing variables and outliers to maintain dataset integrity.",
    "• Conducted Exploratory Data Analysis (EDA) on client datasets to identify underlying performance metrics and correlation coefficients.",
    "• Built interactive analytics reports and business dashboards using Power BI and Microsoft Excel to track KPIs for stakeholders.",
    "• Formulated and optimized MySQL database queries to retrieve and filter data efficiently, reducing report generation cycles.",
    "• Translated data findings into clear, logical insights to support the decision-making process for client business strategies."
]
for b in bullets_int1:
    story.append(Paragraph(b, bullet_style))

story.append(Spacer(1, 2))

intern_2 = [
    [Paragraph("<b>Elite Tech</b>", body_style), Paragraph("<b>01/06/2026 – 03/07/2026</b>", ParagraphStyle('R7', parent=body_style, alignment=2))],
    [Paragraph("<i>Data Science Intern</i>", body_style), Paragraph("<i>Remote</i>", ParagraphStyle('R8', parent=body_style, alignment=2))]
]
t_int2 = Table(intern_2, colWidths=[390, 160])
t_int2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('PADDING', (0,0), (-1,-1), 0)]))
story.append(t_int2)

bullets_int2 = [
    "• Built and evaluated ML models (Logistic Regression, Random Forest) using Scikit-Learn to conduct Predictive Churn Analysis.",
    "• Developed an interactive executive sales dashboard using Dash and Plotly to track transactional performance metrics and territories.",
    "• Implemented an NLP Sentiment Analyzer on customer reviews by applying TF-IDF vectorization and word coefficient visualizations.",
    "• Processed and analyzed massive datasets utilizing PySpark (Big Data) to extract transaction trends and sales KPIs."
]
for b in bullets_int2:
    story.append(Paragraph(b, bullet_style))

# Skills
story.append(Paragraph("SKILLS", heading_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#333333'), spaceAfter=2, spaceBefore=1))
story.append(Paragraph("<b>Technical Skills:</b> Python, NumPy, Pandas, Matplotlib, SciPy, Microsoft Excel, MySQL, Data Visualisation, PowerBI", body_style))
story.append(Paragraph("<b>Behavioral Skills:</b> Analytical Thinking, Problem Solving, Critical Thinking, Decision Making, Creativity, Active Listening, Finds Logical Insights", body_style))

# Projects
story.append(Paragraph("PROJECTS", heading_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#333333'), spaceAfter=2, spaceBefore=1))
story.append(Paragraph("<b>IPL Capstone Analysis</b> | <i>Python, Pandas, NumPy, Matplotlib, Seaborn</i>", body_style))
bullets_p1 = [
    "• Conducted comprehensive data cleaning and preprocessing on the IPL 2022 dataset, handling null values and cleaning match records for consistent analysis.",
    "• Analyzed and visualized match outcome factors, toss decision trends (field vs. bat), and the statistical impact of toss wins on match results using Seaborn.",
    "• Evaluated player metrics by grouping and aggregating data to extract top scorers, wicket-takers (using custom lambda functions to parse bowling figures), and Top 10 Player-of-the-Match awards."
]
for b in bullets_p1:
    story.append(Paragraph(b, bullet_style))

story.append(Spacer(1, 2))
story.append(Paragraph("<b>Zomato Analysis</b> | <i>Python, Pandas, NumPy, Matplotlib, Seaborn</i>", body_style))
bullets_p2 = [
    "• Investigated customer ordering trends and restaurant types, demonstrating that Dining restaurants received the highest votes and consumer engagement.",
    "• Analyzed couple spending habits by plotting the distribution of approximate cost for two and segmenting customer capacity based on cost patterns.",
    "• Built pivot tables and heatmaps to segment offline vs. online ordering behavior, showing that dining places prefer offline visits while cafes drive online deliveries.",
    "• Utilized boxplots and histograms to evaluate customer rating distributions and compared ratings of online versus offline dining options."
]
for b in bullets_p2:
    story.append(Paragraph(b, bullet_style))

# Certifications
story.append(Paragraph("CERTIFICATIONS", heading_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#333333'), spaceAfter=2, spaceBefore=1))
certs = [
    "• <b>Deloitte Data Analytics Job Simulation Certificate</b> - Issued by Forage (June 2026)",
    "• <b>Explore AI Basics</b> - Issued by Microsoft Learn (May 2026)",
    "• <b>Explore Generative AI</b> - Issued by Microsoft Learn (May 2026)",
    "• <b>Pitch It Up (Participation)</b> - Organized under Google Student Campus Ambassador Program (May 2026)"
]
for c in certs:
    story.append(Paragraph(c, bullet_style))

doc.build(story)
print("Updated 2-Line Header Resume Generated!")
