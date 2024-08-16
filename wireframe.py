from matplotlib import pyplot as plt

def draw_dashboard_wireframe():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    ax.text(0.5, 0.95, 'Main Dashboard', fontsize=16, fontweight='bold', ha='center')
    ax.text(0.1, 0.9, 'Inspection Hero', fontsize=12, ha='left')
    ax.text(0.9, 0.9, 'Toolbox | Team Management | Reports | Upgrades', fontsize=10, ha='right')
    ax.plot([0.05, 0.95], [0.88, 0.88], color='black')

    for i in range(3):
        for j in range(3):
            x = 0.1 + j*0.25
            y = 0.7 - i*0.2
            ax.add_patch(plt.Rectangle((x, y), 0.2, 0.15, edgecolor='black', facecolor='none'))
            ax.text(x+0.1, y+0.075, 'Machine', fontsize=10, ha='center', va='center')
            ax.text(x+0.1, y-0.02, 'Status: OK', fontsize=8, ha='center', va='center')
    ax.add_patch(plt.Rectangle((0.05, 0.05), 0.9, 0.1, edgecolor='black', facecolor='none'))
    ax.text(0.1, 0.1, 'Progress Bar: [=====-----]', fontsize=10, ha='left')
    ax.text(0.5, 0.1, 'Currency: 1200', fontsize=10, ha='center')
    ax.text(0.9, 0.1, 'Tasks: 3/5', fontsize=10, ha='right')
    ax.axis('off')
    plt.show()

def draw_inspection_wireframe():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.text(0.5, 0.95, 'Inspection Screen', fontsize=16, fontweight='bold', ha='center')
    ax.add_patch(plt.Rectangle((0.05, 0.4), 0.6, 0.5, edgecolor='black', facecolor='none'))
    ax.text(0.35, 0.65, 'Machine Overview', fontsize=14, fontweight='bold', ha='center')
    ax.text(0.35, 0.6, 'Component 1', fontsize=10, ha='center')
    ax.text(0.35, 0.55, 'Component 2', fontsize=10, ha='center')
    ax.text(0.35, 0.5, 'Component 3', fontsize=10, ha='center')
    ax.add_patch(plt.Rectangle((0.7, 0.4), 0.25, 0.5, edgecolor='black', facecolor='none'))
    ax.text(0.825, 0.9, 'Inspection Tools', fontsize=14, fontweight='bold', ha='center')
    ax.text(0.825, 0.8, 'Tool 1', fontsize=10, ha='center')
    ax.text(0.825, 0.75, 'Tool 2', fontsize=10, ha='center')
    ax.text(0.825, 0.7, 'Tool 3', fontsize=10, ha='center')
    ax.add_patch(plt.Rectangle((0.05, 0.15), 0.3, 0.2, edgecolor='black', facecolor='none'))
    ax.text(0.2, 0.3, 'Condition Indicators', fontsize=14, fontweight='bold', ha='center')
    ax.text(0.2, 0.25, 'Temperature: Normal', fontsize=10, ha='center')
    ax.text(0.2, 0.2, 'Pressure: Normal', fontsize=10, ha='center')
    ax.add_patch(plt.Rectangle((0.4, 0.15), 0.5, 0.2, edgecolor='black', facecolor='none'))
    ax.text(0.65, 0.3, 'Inspect | Repair | Report', fontsize=12, ha='center')
    ax.axis('off')
    plt.show()

def draw_repair_wireframe():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.text(0.5, 0.95, 'Repair Screen', fontsize=16, fontweight='bold', ha='center')
    ax.add_patch(plt.Rectangle((0.05, 0.4), 0.6, 0.5, edgecolor='black', facecolor='none'))
    ax.text(0.35, 0.65, 'Repair Focus Area', fontsize=14, fontweight='bold', ha='center')
    ax.text(0.35, 0.55, 'Part to Repair', fontsize=10, ha='center')
    ax.add_patch(plt.Rectangle((0.7, 0.4), 0.25, 0.5, edgecolor='black', facecolor='none'))
    ax.text(0.825, 0.9, 'Repair Tools', fontsize=14, fontweight='bold', ha='center')
    ax.text(0.825, 0.8, 'Tool 1', fontsize=10, ha='center')
    ax.text(0.825, 0.75, 'Tool 2', fontsize=10, ha='center')
    ax.text(0.825, 0.7, 'Tool 3', fontsize=10, ha='center')
    ax.add_patch(plt.Rectangle((0.3, 0.3), 0.4, 0.05, edgecolor='black', facecolor='none'))
    ax.text(0.5, 0.325, 'Repair Progress: [====------]', fontsize=10, ha='center')
    ax.add_patch(plt.Rectangle((0.4, 0.15), 0.2, 0.1, edgecolor='black', facecolor='none'))
    ax.text(0.5, 0.2, 'Complete Repair', fontsize=12, ha='center')
    ax.axis('off')
    plt.show()

draw_dashboard_wireframe()
draw_inspection_wireframe()
draw_repair_wireframe()
