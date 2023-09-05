import plotly.offline as pyo
import plotly.graph_objs as go

input_html_file = 'side_by_side_plots.html'

# Create data and layout for the first plot
trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines', name='Plot 1')
layout1 = go.Layout(title='First Plot')
fig1 = go.Figure(data=[trace1], layout=layout1)

# Create data and layout for the second plot
trace2 = go.Bar(x=[1, 2, 3], y=[7, 8, 9], name='Plot 2')
layout2 = go.Layout(title='Second Plot')
fig2 = go.Figure(data=[trace2], layout=layout2)

# Generate HTML for each plot
plot1_html = pyo.plot(fig1, include_plotlyjs=False, output_type='div')
plot2_html = pyo.plot(fig2, include_plotlyjs=False, output_type='div')

# Create an HTML template to arrange the plots side by side
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Side-by-Side Plots</title>
    <style>
        .plot-container {{
            display: inline-block;
            width: 50%;
        }}
    </style>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <div class="plot-container">{plot1_html}</div>
    <div class="plot-container">{plot2_html}</div>
</body>
</html>
"""

# Save the HTML template to a file
with open(input_html_file, 'w') as file:
    file.write(html_template)

import subprocess

# Define the command as a list of strings
command = ["node", "generate_pdf.js"]

# Run the command
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check the return code
if result.returncode == 0:
    print("Command executed successfully")
    print("Output:")
    print(result.stdout)
else:
    print("Command failed with error:")
    print(result.stderr)