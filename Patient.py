import streamlit as st
import pandas as pd
st.set_page_config(page_title="Patient Information Form",
                   page_icon="🧊", initial_sidebar_state="expanded")


st.title("Patient Information Form")
st.caption('This web app is developed by: <span style="font-weight:bold;font-size:20px;">Pankil Soni</span>',unsafe_allow_html=True)
st.divider()

old_df = st.file_uploader("Upload Your old csv file", type=["csv"])
old_df = pd.read_csv(old_df) if old_df is not None else None


st.header("Patient Information")
mrnno = st.number_input("MRN NO", min_value=0)


col1, col2, col3 = st.columns(3)
with col1:
    admit_date = st.date_input("Admit_Date", value=None)
with col2:
    age = st.number_input("Age", min_value=0)
with col3:
    department = st.selectbox(
        "Department", ["Pulmonology", "G1", "ENT", "Orthopedic", "Neurology"])


col1, col2, col3 = st.columns(3)
with col1:
    sex = st.selectbox("Sex", ["Male", "Female"])
with col2:
    patient_name = st.text_input(
        "Patient Name", value="Mrs" if sex == "Female" else "Mr")
with col3:
    ward = st.text_input("Ward", value="Executive")

st.divider()

diagnosis = st.text_input("Diagnosis")

surgery = st.radio("Surgery", ["YES", "NO"], index=1)
if surgery == "YES":
    surgery_details = st.text_input("Details")
else:
    surgery_details = None

st.divider()
st.header("Antibiotics Prescribed")

medicines_qty = st.number_input("How many antibiotics", min_value=1, value=1)

antibiotic_cols_name = st.columns(medicines_qty)
antibiotic_cols_dose = st.columns(medicines_qty)
antibiotic_cols_route = st.columns(medicines_qty)
antibiotic_cols_interval = st.columns(medicines_qty)
antibiotic_cols_start_date = st.columns(medicines_qty)
antibiotic_cols_end_date = st.columns(medicines_qty)

Antibiotics_prescribed = ""
Dose = ""
Route = ""
Interval = ""
Start_Date = ""
End_Date = ""

for i in range(medicines_qty):
    with antibiotic_cols_name[i]:
        name = st.text_input(f"Name {i+1}")
        Antibiotics_prescribed = Antibiotics_prescribed + name + ", "

for i in range(medicines_qty):
    with antibiotic_cols_dose[i]:
        dose = st.text_input(f"Dose {i+1}", value="mg")
        Dose = Dose + dose + ", "

for i in range(medicines_qty):
    with antibiotic_cols_route[i]:
        route = st.text_input(f"Route {i+1}", value="IV")
        Route = Route + route + ", "

for i in range(medicines_qty):
    with antibiotic_cols_interval[i]:
        interval = st.text_input(f"Interval {i+1}", value="1-0-1")
        Interval = Interval + interval + ", "

for i in range(medicines_qty):
    with antibiotic_cols_start_date[i]:
        start_date = st.date_input(f"Start Date {i+1}", value=None)
        Start_Date = Start_Date + str(start_date) + ", "

for i in range(medicines_qty):
    with antibiotic_cols_end_date[i]:
        end_date = st.date_input(f"End Date {i+1}", value=None)
        End_Date = End_Date + str(end_date) + ", "


Antibiotics_prescribed = Antibiotics_prescribed[:-2]
Dose = Dose[:-2]
Route = Route[:-2]
Interval = Interval[:-2]
Start_Date = Start_Date[:-2]
End_Date = End_Date[:-2]

st.write(Antibiotics_prescribed, Dose, Route,Interval,Start_Date,End_Date)


st.divider()
st.header("Indication for Antibiotics Treatment")

indications = ["Prophylaxis", "Urinary Tract Infection", "Pneumonia", "Gastrointestinal Infection",
               "Bloodstream Infection", "CNS", "Skin Infection", "Bone Infection", "Respiratory Infection", "Others"]
indication_list = []
cols_1 = st.columns(len(indications)//2)
cols_2 = st.columns(len(indications)//2)

for i, col in enumerate(cols_1):
    with col:
        indication = st.checkbox(indications[i])
        if indication:
            indication_list.append(indications[i])

for i, col in enumerate(cols_2):
    with col:
        indication = st.checkbox(indications[i+len(cols_1)])
        if indication:
            indication_list.append(indications[i+len(cols_1)])

if "Others" in indication_list:
    indication_list.remove("Others")
    others = st.text_input("Others")
    indication_list.append(others)

indication_list = ", ".join(indication_list)

st.divider()
st.header("Initial Review of Antibiotic Treatment")

col_review_1 = st.columns(3)

with col_review_1[0]:
    documented = st.text_input(
        "Is indication for antibiotic treatment documented?", value="NO")

with col_review_1[1]:
    guidelines = st.radio(
        "Is antibiotic treatment prescribed according to guidelines?", ["YES", "NO"], index=None)
    if guidelines == "NO":
        with col_review_1[2]:
            guidelines_comments = st.text_input("Why not?")
    else:
        guidelines_comments = None

col_review_2 = st.columns(3)


with col_review_2[0]:
    correct_dose = st.radio(
        "Correct Dose", ["YES", "NO"], index=None)

with col_review_2[1]:
    appropriate_route = st.radio(
        "Appropriate Route", ["YES", "NO"], index=None)
with col_review_2[2]:
    review_date_stated = st.radio(
        "Treatment Durn/Review Dt Stated", ["YES", "NO"], index=None)

st.divider()
st.header("48-hours Review of Antibiotic Treatment")


treatment_reviewed = st.radio(
    "Is antibiotic treatment reviewed in 48 hours?", ["YES", "NO"], index=None)
if treatment_reviewed == "YES":
    reviewed_in_48_hours = st.selectbox("What action taken?", [
                                        "Escalate", "Continue", "De-escalate", "Stop", "IV oral switch"])
else:
    reviewed_in_48_hours = None

st.write("why is antibiotic treatment being continued?")

continuation_options = [
    "Continuing clinical signs of Infection", "Confirmed Infection", "other"]
continuations_list = []

cols = st.columns(3)

for i in range(len(continuation_options)):
    with cols[i]:
        continuation = st.checkbox(continuation_options[i])
        if continuation:
            continuations_list.append(continuation_options[i])

if "other" in continuations_list:
    continuations_list.remove("other")
    others = st.text_input("Add Reason here")
    continuations_list.append(others)
else:
    continuation_reason_other = None

continuations_list = ", ".join(continuations_list)

st.divider()
st.header("Microbiology Test")
date_nos = st.number_input("How many Microbiology Tests", min_value=0, value=0)

if date_nos > 0:
    col_micro = st.columns(date_nos)

microbiology_specimens_date = ""
microbiology_results_received_date = ""
microbiology_results_acted_upon=""

if date_nos > 0:
    for i in range(date_nos):
        with col_micro[i]:
            date = st.date_input(f"microbiology_specimens_date {i+1}", value=None)
            microbiology_specimens_date = microbiology_specimens_date + \
                str(date)+", "

    for i in range(date_nos):
        with col_micro[i]:
            date = st.date_input(
                f"microbiology_results_received_date {i+1}", value=None)
            microbiology_results_received_date = microbiology_results_received_date + \
                str(date)+", "
            
    microbiology_results_acted_upon = st.text_input(
    "Microbiology Results Acted Upon", value="Based on culture test")

microbiology_specimens_date = microbiology_specimens_date[:-2]
microbiology_results_received_date = microbiology_results_received_date[:-2]


st.divider()
st.header("Culture Test")
cut_num = st.number_input("How many culture tests", min_value=0, value=0)

if cut_num > 0:
    culture_cols_date = st.columns(cut_num)

culture_test_date = ""
culture_test_sample= ""
culture_test_organism = ""

if cut_num > 0:

    for i in range(cut_num):
        with culture_cols_date[i]:
            date = st.date_input(f"culture_test_date {i+1}", value=None)
            culture_test_date = culture_test_date + str(date)+", "

    culture_test_date = culture_test_date[:-2]

    culture_test_sample = st.text_input("Culture test sample", value=None)

    culture_test_organism = st.text_input("Culture test organism", value=None)

st.divider()

source_of_infection = st.text_input("Source of infection", value="")

gram_negative_cover_or_gram_postive_cover = st.text_input(
    "Gram negative cover or gram postive cover", value="")

appropiate_indication_for_antimicribial_agents_use = st.text_input(
    "Appropiate indication for antimicribial agents use", value="")

st.divider()
st.header("Discharge Information")
discharge_date = st.date_input("Discharge Date", value=None)
discharge_medication = st.text_input("Discharge Medication")
complaints = st.text_input("Complaints")

columns = old_df.columns if old_df is not None else ["MRN no.", "Patient name", "Age", "Sex", "Department", "Ward", "pt adm date", "pt dis date", "C/O", "Diagnosis", "Surgery", "Antibiotics prescribed", "Dose", "Route", "Interval", "Start date", "stop date", "Indication for antibiotic Treatment", "Is indication for antibiotic treatment documented?", "Is antibiotic Treatment Prescribed according to guidelines?", " If not? Comment", "If yes? Correct dose?", "Appropriate route?",
                                                     "Treatment duration or review date stated?", "Is antibiotic treatment reviewed in 48 hours?", "If yes what action?", "Why antibiotic treatment being continued?", "Discharge Medications", "Microbiology specimens collected date?", "Microbiology results received date?", "Microbiology results acted upon?", "Culture test date", "Culture test sample", "culture test organism", "Source of infection", "Gram negative cover or gram postive cover", "Appropiate indication for antimicribial agents use"]

one_row_data = [
    mrnno,  # MRN no.
    patient_name,  # Patient Name
    age,  # Age
    sex,  # Sex
    department,  # Department
    ward,  # Ward
    admit_date,  # pt adm date
    discharge_date,  # pt dis date
    complaints,  # C/O
    diagnosis,  # Diagnosis
    surgery,  # Surgery
    Antibiotics_prescribed,  # Antibiotics Prescribed
    Dose,  # Dose
    Route,  # Route
    Interval,  # Interval
    Start_Date,  # Start_Date
    End_Date,  # End_date
    indication_list,  # Indications for Antibiotics Treatment
    documented,  # Is indication for antibiotic treatment documented?
    guidelines,  # Is antibiotic treatment prescribed according to guidelines?
    guidelines_comments,  # Guidelines Comments
    correct_dose,  # Correct Dose
    appropriate_route,  # Appropriate Route
    review_date_stated,  # Treatment Durn/Review Dt Stated
    treatment_reviewed,  # Is antibiotic treatment reviewed?
    reviewed_in_48_hours,  # Is antibiotic treatment reviewed in 48 hours?
    continuations_list,  # Why is antibiotic treatment being continued?
    discharge_medication,  # Discharge Medications
    microbiology_specimens_date,  # Microbiology Specimens Date
    microbiology_results_received_date,  # Microbiology Results Received Date
    microbiology_results_acted_upon,  # Microbiology Results Acted Upon
    culture_test_date,  # Culture test date
    culture_test_sample,  # Culture test sample
    culture_test_organism,  # Culture test organism
    source_of_infection,  # Source of infection
    # Gram negative cover or gram postive cover
    gram_negative_cover_or_gram_postive_cover,
    # Appropiate indication for antimicribial agents use
    appropiate_indication_for_antimicribial_agents_use
]

if 'new_added_rows' not in st.session_state:
    st.session_state.new_added_rows = pd.DataFrame(columns=columns)

if st.button("Add Data"):
    df_n = pd.DataFrame([one_row_data], columns=columns)
    st.session_state.new_added_rows.loc[len(
        st.session_state.new_added_rows)] = df_n.iloc[0]

# Display New Added Rows
st.divider()
st.header("New Added Rows")
st.write(st.session_state.new_added_rows)

if st.button("Remove Last Added Row"):
    st.session_state.new_added_rows = st.session_state.new_added_rows[:-1]
    st.rerun()

st.divider()

if old_df is not None:
    if st.button("Download Merged CSV"):
        updated_csv = pd.concat([old_df, st.session_state.new_added_rows])
        st.write(updated_csv)
    st.divider()

st.caption('This web app is developed by: <span style="font-weight:bold;font-size:20px;">Pankil M Soni</span>',unsafe_allow_html=True)