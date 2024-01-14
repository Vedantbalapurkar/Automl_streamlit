#command -   streamlit run store.py --server.enableXsrfProtection=false
import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from pycaret.regression import setup, compare_models, pull, save_model
import os
from streamlit.components.v1 import components
#from autoviz import AutoViz_Class, data_cleaning_suggestions
import time
import sweetviz as sv
#import pandas_profiling
#st.set_page_config(layout="wide")
# Set page configuration

# Create an instance of AutoViz_Class
#AV = AutoViz_Class()

st.set_page_config(
    page_title="My Streamlit App",  # The title of the browser tab
    page_icon=":chart_with_upwards_trend:",  # A favicon icon for the app
    layout="wide",  # Layout style ("wide" or "centered")
    initial_sidebar_state="expanded"  # Initial state of the sidebar ("expanded" or "collapsed")
)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

# _, col2, _ = st.columns([1, 2, 1])
# with col2:
#     #st.title("This is my heading")
# colT1,colT2 = st.columns([1,5])
# with colT2:
    #st.title(“Major Consumer Bundle Analysis”)


st.header("🚀 Auto-ML Streamlit App", divider='rainbow')
#st.header("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)

# st.text("")
# st.text("")
# st.text("")
# st.text("")
tab_titles = ['Home','Visualization','Profiling','Modelling','Download','About']
tabs = st.tabs(tab_titles)
font_css = """
<style>
button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
  font-size: 25px;
  text-align: center;
}
</style>
"""
st.write(font_css, unsafe_allow_html=True)


with tabs[3]:
    st.error("Modeling section are under development. Coming soon!")

with tabs[4]:
    st.error("Download section are under development. Coming soon!")

with tabs[5]:
    st.markdown("## About Auto-ML Streamlit App 🌐✨")

    st.markdown("Welcome to the About section! Here, we provide some background and information about our Auto-ML Streamlit App.")

    st.subheader("Purpose:")
    st.write("Our app is designed to simplify the machine learning workflow, making it accessible to users with varying levels of expertise. We aim to provide a user-friendly platform for data exploration, automated data preprocessing, efficient modeling, and easy access to customized machine learning models.")

    st.subheader("Team:")
    st.write("Auto-ML Streamlit App is developed and maintained by a dedicated team of machine learning enthusiasts. Meet our core team members:")
    st.write("- [Vedant Balapurkar](#)")
    #st.write("- [Team Member 2](#)")
    #st.write("- [Team Member 3](#)")

    st.subheader("Acknowledgments:")
    st.write("We would like to express our gratitude to the open-source community and contributors who have played a crucial role in the development of this app. Additionally, we appreciate the support and feedback from our users, helping us improve and enhance the app.")

    st.subheader("Contact Us:")
    st.write("If you have any questions, suggestions, or feedback, feel free to reach out to us:")
    st.write("- Email: [vedantbalapurkar1234@gmail.com](mailto:vedantbalapurkar1234@gmail.com)")
    st.write("- Twitter: [@AutoMLStreamlit](https://twitter.com/AutoMLStreamlit)")


# Function to load data from a CSV file
with tabs[0]:
    #st.headre("🚀 Auto-ML Streamlit App")
    st.markdown("Discover the future of machine learning with our cutting-edge Auto-ML Streamlit App. 🌐✨")

    st.subheader("Key Features:")
    st.markdown("1. **Effortless Data Visualization:**\n"
                "   - 📊 Upload your dataset seamlessly.\n"
                "   - 📈 Explore data insights with a variety of chart types.")
    
    st.markdown("2. **Automated Data Preprocessing:**\n"
                "   - 🧹 Let the app handle data preprocessing tasks.\n"
                "   - 🔍 Utilize data profiling for in-depth analysis.")
    
    st.markdown("3. **Modeling Efficiency:**\n"
                "   - ⚙️ Build machine learning models effortlessly.\n"
                "   - 🚀 Explore diverse algorithms with a few clicks.")

    st.markdown("4. **Customized Machine Learning Models:**\n"
                "   - 🛠️ Tailor models to your needs.\n"
                "   - 📊 Visualize performance metrics for easy comparison.")

    st.markdown("5. **User-Friendly Interface:**\n"
                "   - 🎨 Intuitive and user-friendly design.\n"
                "   - 🌈 Access advanced features seamlessly.")
    

with tabs[2]:
    st.subheader("Exploratory Data Analysis")

    # File uploader for dataset
    st.markdown("Upload Your Dataset")
    file1 = st.file_uploader("")

    # Create columns for layout
    col1, col2, col3, col4, col5 = st.columns([1, 1.3, 1, 1, 1])  # Adjust column ratios as needed

    with col3:
        # Centered button to trigger analysis
        st.markdown("")
        st.markdown("")
        st.markdown("")
        if st.button("Generate Analysis"):
            
            with st.spinner(text="Generating"):
                time.sleep(5)
            #st.write("Analysis in progress...")

            # Perform Sweetviz analysis
    if file1:
        df = pd.read_csv(file1, index_col=None)
        df.to_csv('dataset.csv', index=None)
        my_report = sv.analyze(df)

                    # Save the Sweetviz report to a temporary HTML file
        report_path = "temp_report.html"
        my_report.show_html(report_path)

                    # Read the content of the HTML file
        with open(report_path, "r", encoding="utf-8") as report_file:
            report_content = report_file.read()

                    # Display the Sweetviz report in Streamlit using components
        st.components.v1.html(report_content, width=2000, height=2000)

        #st.write("Analysis completed!")



# Optionally, you can remove the temporary HTML file after displaying the report
# import os
        #os.remove(report_path)








# with tabs[2]:
#     st.title("AutoViz Profiling")

#     # Upload dataset for AutoViz profiling
#     file_auto_viz = st.file_uploader("Upload Your Dataset for AutoViz Profiling", type=["csv", "txt", "json"])

#     if file_auto_viz:
#         # Read the uploaded file
#         df_auto_viz = pd.read_csv(file_auto_viz)
        
#         # Perform AutoViz profiling
#         st.subheader("AutoViz Profiling Results")
        
#         # You can customize the AutoViz settings based on your requirements
#         dft_auto_viz = AV.AutoViz(
#             filename='',
#             sep=',',
#             depVar='',
#             dfte=df_auto_viz,
#             header=0,
#             verbose=2,
#             lowess=False,
#             chart_format='png',  # Choose the format you prefer (png, svg, jpg, bokeh, server, or html)
#             max_rows_analyzed=150000,
#             max_cols_analyzed=30,
#             save_plot_dir=None
#         )
        
#         # Display or save the AutoViz profiling results
#         # You can customize how you want to show the results, such as using st.image() or st.components.v1.html()

#         # Example using st.image()
#         #st.image('path/to/auto_viz_output.png', caption='AutoViz Profiling Results', use_column_width=True)

#                # Display the AutoViz profiling results
#         # st.subheader("AutoViz Profiling Results")
#         st.components.v1.html(dft_auto_viz.to_html(), width=1000, height=6000)
        #st.image(dft_auto_viz, caption='AutoViz Profiling Results', use_column_width=True)

        

with tabs[1]:
    def load_csv_data():
        uploaded_file = st.file_uploader("Upload CSV File", type=["csv"], key="csv_uploader")

        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                return df
            except Exception as e:
                st.error(f"Error loading CSV file: {e}")
                return pd.DataFrame()

        return None

    # Function to load sample data from Plotly Express
    @st.cache_data()#allow_output_mutation=True)
    def load_sample_data():
        return px.data.iris()

    # Function to generate the chart based on user input
    def generate_chart(df, chart_type, selected_columns):
        #st.subheader(f'{chart_type} Configuration')

        try:
            if chart_type == 'Scatter Plot':
                if len(selected_columns) >= 2:
                    fig = px.scatter(df, x=selected_columns[0], y=selected_columns[1], color=selected_columns[2])
                else:
                    st.warning("Please select at least two columns for the Scatter Plot.")

            elif chart_type == 'Scatter Plot with Marginals':
                if len(selected_columns) >= 2:
                    fig = px.scatter(df, x=selected_columns[0], y=selected_columns[1], color=selected_columns[2],
                                marginal_y="violin", marginal_x="box", trendline="ols", template="simple_white")
                else:
                    st.warning("Please select at least two columns for Scatter Plot with Marginals.")

            elif chart_type == 'Scatter Plot with Error Bars':
                if len(selected_columns) >= 2:
                    df["e"] = df[selected_columns[0]] / 100
                    fig = px.scatter(df, x=selected_columns[0], y=selected_columns[1], color=selected_columns[2] if len(selected_columns) > 2 else None,
                                error_x="e", error_y="e")
                else:
                    st.warning("Please select at least two columns for Scatter Plot with Error Bars.")

            elif chart_type == 'Grouped Bar Chart':
                if len(selected_columns) >= 2:
                    fig = px.bar(df, x=selected_columns[0], y=selected_columns[1], color=selected_columns[2] if len(selected_columns) > 2 else None, barmode="group")
                else:
                    st.warning("Please select at least two columns for Grouped Bar Chart.")

            elif chart_type == 'Patterned Bar Chart':
                if len(selected_columns) >= 2:
                    fig = px.bar(df, x=selected_columns[0], y=selected_columns[1], color=selected_columns[2] if len(selected_columns) > 2 else None,
                            pattern_shape=selected_columns[2] if len(selected_columns) > 2 else None, pattern_shape_sequence=[".", "x", "+"])
                else:
                    st.warning("Please select at least two columns for Patterned Bar Chart.")

            elif chart_type == 'Faceted Bar Chart':
                if len(selected_columns) >= 3:
                    if len(selected_columns) > 4:
                        fig = px.bar(df, x=selected_columns[0], y=selected_columns[1], color=selected_columns[2] if len(selected_columns) > 2 else None,
                                barmode="group", facet_row=selected_columns[3], facet_col=selected_columns[4],
                                category_orders={selected_columns[4]: ["Thur", "Fri", "Sat", "Sun"],
                                                selected_columns[3]: ["Lunch", "Dinner"]})
                    else:
                        fig = px.bar(df, x=selected_columns[0], y=selected_columns[1], color=selected_columns[2] if len(selected_columns) > 2 else None,
                                barmode="group")
                else:
                    st.warning("Please select at least three columns for Faceted Bar Chart.")

            elif chart_type == 'Scatter Matrix':
                if len(selected_columns) >= 2:
                    fig = px.scatter_matrix(df, dimensions=selected_columns, color=selected_columns[0])
                else:
                    st.warning("Please select at least two columns for Scatter Matrix.")

            elif chart_type == 'Parallel Coordinates':
                if len(selected_columns) >= 2:
                    fig = px.parallel_coordinates(df, color=selected_columns[0])
                else:
                    st.warning("Please select at least two columns for Parallel Coordinates.")

            elif chart_type == 'Parallel Categories':
                if len(selected_columns) >= 1:
                    fig = px.parallel_categories(df, color=selected_columns[0], color_continuous_scale=px.colors.sequential.Inferno)
                else:
                    st.warning("Please select at least one column for Parallel Categories.")

            elif chart_type == 'Bubble Chart':
                if len(selected_columns) >= 5:
                    fig = px.scatter(df, x=selected_columns[0], y=selected_columns[1], size=selected_columns[2], color=selected_columns[3],
                                hover_name=selected_columns[4], log_x=True, size_max=60)
                else:
                    st.warning("Please select at least five columns for Bubble Chart.")

            elif chart_type == 'Animated Scatter Chart':
                if len(selected_columns) >= 8:
                    fig = px.scatter(df, x=selected_columns[0], y=selected_columns[1], animation_frame=selected_columns[2],
                                animation_group=selected_columns[3], size=selected_columns[4], color=selected_columns[5],
                                hover_name=selected_columns[6], facet_col=selected_columns[7],
                                log_x=True, size_max=45, range_x=[100, 100000], range_y=[25, 90])
                else:
                    st.warning("Please select at least eight columns for Animated Scatter Chart.")

            elif chart_type == 'Line Chart':
                if len(selected_columns) >= 5:
                    fig = px.line(df, x=selected_columns[0], y=selected_columns[1], color=selected_columns[2], line_group=selected_columns[3],
                            hover_name=selected_columns[4], line_shape="spline", render_mode="svg")
                else:
                    st.warning("Please select at least five columns for Line Chart.")

            elif chart_type == 'Area Chart':
                if len(selected_columns) >= 4:
                    fig = px.area(df, x=selected_columns[0], y=selected_columns[1], color=selected_columns[2], line_group=selected_columns[3])
                else:
                    st.warning("Please select at least four columns for Area Chart.")

            elif chart_type == 'Timeline':
                if len(selected_columns) >= 3:
                    fig = px.timeline(df, x_start=selected_columns[0], x_end=selected_columns[1], y=selected_columns[2], color=selected_columns[2])
                else:
                    st.warning("Please select at least three columns for Timeline.")

            elif chart_type == 'Funnel Chart':
                if len(selected_columns) >= 2:
                    fig = px.funnel(df, x=selected_columns[0], y=selected_columns[1])
                else:
                    st.warning("Please select at least two columns for Funnel Chart.")

            elif chart_type == 'Pie Chart':
                if len(selected_columns) >= 3:
                    fig = px.pie(df, values=selected_columns[0], names=selected_columns[1], title=selected_columns[2])
                else:
                    st.warning("Please select at least three columns for Pie Chart.")

            elif chart_type == 'Sunburst Chart':
                if len(selected_columns) >= 2:
                    fig = px.sunburst(df, path=[px.Constant("all"), selected_columns[0]], values=df[selected_columns[1]])
                else:
                    st.warning("Please select at least two columns for Sunburst Chart.")


            col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])  # Adjust column ratios as needed

            with col3:
        # Centered button to trigger analysis
                # if st.button("Generate Analysis"):
                #     st.write("Analysis in progress...")

            # Display the chart
                if 'fig' in locals():
                    st.subheader(f"{chart_type}")
                
            col1, col2, col3, col4, col5 = st.columns([0.5, 0.5, 1, 1, 1])  # Adjust column ratios as needed

            with col3:    

                if 'fig' in locals():
                    st.plotly_chart(fig)

        except Exception as e:
            # Display a user-friendly error message
            st.error(f"An error occurred: {e}")
   # Function to load sample data from Plotly Express
    @st.cache_data(hash_funcs={type(px.data.iris()): lambda x: None})
    def load_sample_data():
        return px.data.iris()
    # Main function for Streamlit app
    def main():
        st.subheader('Interactive Chart Generator')
        #st.subheader("Choose Data Source")
        data_source = st.radio("Choose Data Source",["Upload New File", "Sample Data"])

        # Load data based on user's choice
        if data_source == "Upload New File":
            df = load_csv_data()
        else:
            df = load_sample_data()

        # Display the loaded DataFrame
        # st.write(df)

        # Add "See Raw Data" expander with custom size
        row3_1, row3_2 = st.columns((100, 2))

        with row3_1:
            st.markdown("")
            see_data = st.expander('You can click here to see the raw data first 👉', expanded=False)
            with see_data:
                # Check if df is not None before using head method
                if df is not None:
                    # Adjust the number of rows displayed in the DataFrame
                    st.dataframe(data=df.head(1000).reset_index(drop=True))  # Displaying the first 1000 rows as an example
                    # Customizing the width of the expander
                    st.markdown("<style>.streamlit-expander {width: 720px;}</style>", unsafe_allow_html=True)
                else:
                    st.warning("Please upload or select a dataset.")

        # Choose chart type
        #st.write("Select Chart Type")
        chart_type = st.selectbox("Select Chart Type", [
            'Scatter Plot',
            'Scatter Plot with Marginals',
            'Scatter Plot with Error Bars',
            'Grouped Bar Chart',
            'Patterned Bar Chart',
            'Faceted Bar Chart',
            'Scatter Matrix',
            'Parallel Coordinates',
            'Parallel Categories',
            'Bubble Chart',
            'Animated Scatter Chart',
            'Line Chart',
            'Area Chart',
            'Timeline',
            'Funnel Chart',
            'Pie Chart',
            'Sunburst Chart'
        ])

        # Columns selection dropdown
        if df is not None:
            selected_columns = st.multiselect("Select Columns", df.columns.tolist(), default=df.columns.tolist()[:2])
        else:
            selected_columns = []

        # Submit button to generate chart
        if st.button("Generate Chart"):
            with st.spinner(text="Generating"):
                time.sleep(3)
                #st.success("Generated")
            generate_chart(df, chart_type, selected_columns)

# Run the app
    if __name__ == "__main__":
        main()
