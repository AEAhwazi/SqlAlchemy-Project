import streamlit as st
import app_data


st.title('Khaneh Branameh Nevisan')
st.success('In this APP you can do operation about [Student/Course/Class]')

menu = st.sidebar.radio('Select Option:', ('Lesson', 'Student'))


if menu == 'Lesson':
    option_lesson = st.sidebar.selectbox('Lesson', ('Add', 'Edit', 'Delete'))

    if option_lesson == 'Add':
        with st.form('Please enter new record:'):
            #v_lesson_id = st.number_input('Enter lesson id:', value=None)
            v_title = st.selectbox('Please select lesson', (
                                                            'Mathmatic',
                                                            'Physic',
                                                            'Chemestry',
                                                            'English'))
            v_unit = st.number_input('Enter lesson unit:')
                    
            submit = st.form_submit_button('Save Racord')
            if submit:
                #result = app_data.add_record_lesson(v_lesson_id, v_title, v_unit)
                result = app_data.add_record_lesson(v_title, v_unit)
                st.sidebar.success('Record saved!')

    if option_lesson == 'Edit':
        pass
        
    if option_lesson == 'Delete':
        pass

if menu == 'Student':
    option_student = st.sidebar.selectbox('Student', ('Add', 'Edit', 'Delete'))

    if option_student == 'Add':
        with st.form('Please enter new record:'):
            col1, col2 = st.columns(2)

            with col1:
                #v_student_id = st.number_input('Enter student id:', value=None)
                v_name = st.text_input('Enter student name:')
                v_gender = st.radio('Gender:', ('Male', 'Femail'))

            with col2:
                v_phone = st.text_input('Enter phone number:')
                v_address = st.text_input('Enter address:')
        
            submit = st.form_submit_button('Save Racord')
            if submit:
                #result = app_data.add_record_student(v_student_id, v_name, v_gender, v_phone, v_address)
                result = app_data.add_record_student(v_name, v_gender, v_phone, v_address)
                st.sidebar.success('Record saved!')

    if option_student == 'Edit':
        pass
        
    if option_student == 'Delete':
        v_student_id = st.number_input('Enter student is:', value=None)
        result = app_data.view_record_student(v_student_id)

        if result == False:
            st.sidebar.success("Record Not Found!")

        else:
            st.success(result)
            if st.button("Click to delete record!"):
                del_record = app_data.del_record_student(v_student_id)
                if del_record == True:
                    st.sidebar.success("Record Deleted!")

#End Program.