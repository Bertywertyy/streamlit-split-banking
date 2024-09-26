import streamlit as st

# Get user input for initial balance
x = st.number_input('How much money do you have?', min_value=0, step=1)

# Get the records of income or expenses
record = st.text_area(
    '''Add an expense or income record
    (e.g. "desc1 amt1, desc2 amt2, ...")''', height=100
)

if st.button('Calculate'):
    # Initialize balance
    balance = x

    if record:
        # Process records
        records = [entry.strip() for entry in record.split(',')]
        output = "\n".join(records)

        try:
            # Update balance
            balance += sum(int(entry.rsplit(' ', 1)[1]) for entry in records)

            # Display results
            st.write(f"Here's your expense and income records:\n{output}")
            st.write(f"Now you have {balance} dollars.")
        except ValueError:
            st.error("Please ensure all records are in the correct format (desc amount).")
