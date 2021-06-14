import plotly.express as px
import pandas as pd

vacc = pd.read_csv('Path of the downbloaded vaccination csv file to be inserted here. Be sure to download it from the official WHO website as the column headings must remain intact.')

gropvacc = vacc.groupby(["COUNTRY"])[["TOTAL_VACCINATIONS"]].mean().reset_index()
fig = px.bar(gropvacc[["COUNTRY", "TOTAL_VACCINATIONS"]].sort_values('TOTAL_VACCINATIONS', ascending=False),
                        y="TOTAL_VACCINATIONS", x="COUNTRY", color="COUNTRY",
                        log_y=False, template='ggplot2')
fig.show()
