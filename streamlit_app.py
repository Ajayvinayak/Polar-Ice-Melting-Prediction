import streamlit as st
import pandas as pd
import math

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Sea Ice Data Dashboard',
    page_icon=':snowflake:',  # This is an emoji shortcode. Could be a URL too.
)

# ---------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_sea_data(uploaded_file, file_type):
    """Grab sea region data from an uploaded file (CSV, XLS, XLSX)."""
    if file_type == "csv":
        raw_df = pd.read_csv(uploaded_file)
    elif file_type in ["xls", "xlsx"]:
        raw_df = pd.read_excel(uploaded_file)
    else:
        raise ValueError("Unsupported file type")
    return raw_df

# File upload widget
uploaded_file = st.file_uploader("Upload your sea region data file", type=["csv", "xls", "xlsx"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()
    sea_df = get_sea_data(uploaded_file, file_type)

    # ---------------------------------------------------------------------
    # Draw the actual page

    # Set the title that appears at the top of the page.
    '''
    # :snowflake: Sea Ice Data Dashboard

    Browse data for various sea regions over the years. This dataset provides measurements for
    regions such as the Sea of Okhotsk, Bering Sea, Hudson Bay, and more, spanning multiple decades.
    '''

    # Add some spacing
    ''
    ''

    # Get the min and max years from the data
    min_value = sea_df['yyyy'].min()
    max_value = sea_df['yyyy'].max()

    # Year selection slider
    from_year, to_year = st.slider(
        'Which years are you interested in?',
        min_value=min_value,
        max_value=max_value,
        value=[min_value, max_value]
    )

    # Extract sea region names (columns excluding 'yyyy' and 'All Regions')
    regions = sea_df.columns[1:-1]

    if not len(regions):
        st.warning("Select at least one sea region")

    # Multi-select for sea regions
    selected_regions = st.multiselect(
        'Which sea regions would you like to view?',
        regions,
        ['Sea of Okhotsk', 'Bering Sea', 'Hudson Bay']
    )

    # Filter the data
    filtered_sea_df = sea_df[
        (sea_df['yyyy'] >= from_year) & (sea_df['yyyy'] <= to_year)
    ]

    st.header('Sea Ice Coverage Over Time', divider='gray')

    # Plot the line chart
    if selected_regions:
        st.line_chart(
            filtered_sea_df.set_index('yyyy')[selected_regions],
        )
    else:
        st.warning("Please select at least one sea region to visualize.")

    ''

    # Summary for the selected years
    first_year = filtered_sea_df[filtered_sea_df['yyyy'] == from_year]
    last_year = filtered_sea_df[filtered_sea_df['yyyy'] == to_year]

    st.header(f'Sea Ice Coverage in {to_year}', divider='gray')

    # Display metrics for each selected sea region
    cols = st.columns(len(selected_regions))

    for i, region in enumerate(selected_regions):
        col = cols[i % len(cols)]

        with col:
            first_coverage = first_year[region].iat[0] / 1000  # Scaling the value (if needed)
            last_coverage = last_year[region].iat[0] / 1000

            if math.isnan(first_coverage):
                growth = 'n/a'
                delta_color = 'off'
            else:
                growth = f'{last_coverage / first_coverage:,.2f}x'
                delta_color = 'normal'

            st.metric(
                label=f'{region} Coverage (1000s sq km)',
                value=f'{last_coverage:,.0f}k',
                delta=growth,
                delta_color=delta_color
            )

 

   
