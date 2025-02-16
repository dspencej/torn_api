import re
from datetime import datetime


def generate_html_log(log_path, output_html):
    """
    Read the log file at log_path, parse each line, and write an HTML report to output_html.
    """
    # Regular expression to parse each log line.
    log_pattern = re.compile(
        r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) \[(?P<level>\w+)\] (?P<message>.*)$"
    )
    entries = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            match = log_pattern.match(line)
            if match:
                entries.append(match.groupdict())
            else:
                entries.append({
                    "timestamp": "",
                    "level": "INFO",
                    "message": line
                })

    html_header = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Log Report</title>
<style>
  body { font-family: Arial, sans-serif; margin: 20px; }
  #searchBox { margin-bottom: 20px; padding: 8px; width: 300px; font-size: 16px; }
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
  th { background-color: #f2f2f2; }
  tr:nth-child(even) { background-color: #f9f9f9; }
  .DEBUG { color: #007bff; }
  .INFO { color: #28a745; }
  .WARNING { color: #ffc107; }
  .ERROR { color: #dc3545; }
</style>
<script>
function filterLogs() {
    var input = document.getElementById("searchBox");
    var filter = input.value.toLowerCase();
    var table = document.getElementById("logTable");
    var tr = table.getElementsByTagName("tr");
    // Skip header row.
    for (var i = 1; i < tr.length; i++) {
        var tds = tr[i].getElementsByTagName("td");
        var rowMatches = false;
        for (var j = 0; j < tds.length; j++) {
            var txtValue = tds[j].textContent || tds[j].innerText;
            if (txtValue.toLowerCase().indexOf(filter) > -1) {
                rowMatches = true;
                break;
            }
        }
        tr[i].style.display = rowMatches ? "" : "none";
    }
}
</script>
</head>
<body>
<h1>Log Report</h1>
<input type="text" id="searchBox" onkeyup="filterLogs()" placeholder="Search logs...">
<table id="logTable">
  <thead>
    <tr>
      <th>Timestamp</th>
      <th>Level</th>
      <th>Message</th>
    </tr>
  </thead>
  <tbody>
"""
    html_footer = """\
  </tbody>
</table>
</body>
</html>
"""
    rows = []
    for entry in entries:
        ts = entry.get("timestamp", "")
        level = entry.get("level", "")
        message = entry.get("message", "")
        try:
            dt = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S,%f")
            ts = dt.strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pass
        row = f"""\
    <tr>
      <td>{ts}</td>
      <td class="{level}">{level}</td>
      <td>{message}</td>
    </tr>
    """
        rows.append(row)

    html_content = html_header + "\n".join(rows) + html_footer
    with open(output_html, "w", encoding="utf-8") as out:
        out.write(html_content)
    print(f"HTML log report generated: {output_html}")
