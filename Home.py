import streamlit as st
from components import footer


def main():
    disclaimer_text = "***Disclaimer: I am not responsible for any damages caused to your academic reputation in any form of plagiarism***"

    st.set_page_config(page_title="LangSphere", page_icon=":brain:")

    st.markdown("<h1 style='text-align: center; color: green;'>Welcome to LangSphere!</h1>",
                unsafe_allow_html=True)

    st.markdown("<h3>Why LangSphere?</h3>", unsafe_allow_html=True)

    st.write("""
    I've noticed that a lot of students and my peers use ChatGPT for pretty much everything, without really exploring all the other cool stuff AI can do.
    Sure, ChatGPT is awesome, but it's just one of the many cool AI tools out there. I wanted to show you all the amazing possibilities.
    So, I created LangSphere as a fun AI playground. It's like your personal tour guide to the world of AI. Here, you can do way more than just basic ChatGPT stuff.
    Think of it as a place where you can dive deep into the world of AI and go on an exciting journey beyond the usual.
    """)

    st.write("""
    I developed LangSphere as an immersive and interactive educational instrument. Within its digital confines, you possess the ability to seamlessly upload files, conduct data analyses, and delve into the intricate world of metrics.
    My overarching objective is to foster and nourish your innate curiosity, igniting those coveted 'a-ha' moments on your journey through the realm of AI. I am here to assist you in elevating your skill set to new heights.
    LangSphere serves as the key to expanding your knowledge base and unlocking your inherent potential. It's an environment where your inner genius can flourish and thrive.
    So, fasten your seatbelts and prepare to embark on a captivating journey into the world of AI, as we delve deep into the intricacies of this fascinating field.
    """)

    st.markdown("---")

    st.markdown("<h3 style='text-align: center; color: green;'>Feature #1 - AskPDF 📚</h3>",
                unsafe_allow_html=True)

    st.write("""
    :one: AskPDF allows you to upload multiple PDFs and ask questions about them. The AI will 
    process the PDFs and give you answers!
    """)

    st.write("""
    For example, say a student has an assignment but doesn't fully understand the requirements.  
    They can upload the assignment PDF and ask questions to clarify what needs to be done.
    """)

    st.markdown('> "When I got my essay assignment, I was so confused. The prompt was kind of fuzzy, and the requirements were all over the place. I ended up tossing the PDF onto AskPDF and asked it to help me figure out what the heck was going on and give me some tips. AskPDF really came through! It broke things down in a simple way and made everything clear as day. Now, I know exactly how to rock this essay!""')

    # st.subheader("Here's how:")
    # video_file = open('./files/pdfpal.mkv', 'rb')
    # video_bytes = video_file.read()
    # st.video(video_bytes)
    # st.markdown(f'<font color="red">{disclaimer_text}</font>', unsafe_allow_html=True)
    # st.markdown("---")

    # Feature 2 - DataLens
    st.markdown("<h3 style='text-align: center; color: green;'>Feature #2 - DataLens</h3>",
                unsafe_allow_html=True)

    st.write("""
    :two: DataLens allows you to analyze and get insights from CSV data. Upload a CSV file and ask questions - 
    the AI will process the data and provide answers!
    """)

    st.write("""
    For a data analytics student immersed in a project, DataLens serves as a valuable tool to uncover hidden trends and patterns that might have eluded their initial observation.
    With DataLens, they can effortlessly upload their CSV dataset and pose insightful questions, allowing for a more profound and structured analysis of the data at hand.
    """)

    st.markdown('> "While working on a class project involving customer data analysis, I found myself drowning in a sea of numbers. That\'s when I stumbled upon DataLens! I promptly uploaded my CSV file and began to inquire. Much to my amazement, DataLens unearthed insights that had previously eluded me, unveiling a wealth of information I would never have spotted on my own. It skillfully distilled retention drivers and churn predictors, providing me with a concise and comprehensive summary.')

    # st.subheader("Here's how:")
    # video_file = open('./files/branhub.mp4', 'rb')
    # video_bytes = video_file.read()
    # st.video(video_bytes)
    st.markdown(
        f'<font color="red">{disclaimer_text}</font>', unsafe_allow_html=True)
    st.markdown("---")

    # Extra Feature - VizTrackr
    st.markdown("<h3 style='text-align: center; color: green;'>Upcoming Feature - VizTrackr</h3>",
                unsafe_allow_html=True)

    st.write("""
    :three: VizTrackr is a fantastic addition to LangSphere, designed specifically to meet the needs of our users. This analytics dashboard lets students dive into their data and really grasp what it's all about. For instance, when you plug in COVID-19 data dating back to 2020, you can see how the pandemic has affected education. It gives you a complete picture with stats on cases, deaths, and other important numbers.
    """)

    st.write("""
    This feature is currently under construction and will soon be available for all types of data, making it even more versatile.
    """)

    st.markdown('''<p style="color:red;">*Dataset used in this dashboard is only up to 23th Aug 2023</p>''',
                unsafe_allow_html=True)

    # Define the JavaScript code for updating the year
    js_code = """
    <script>
        // Get the current year
        const currentYear = new Date().getFullYear();

        // Display the current year in the footer
        document.getElementById("year").textContent = currentYear;
    </script>
    """

    # Add the JavaScript code to the app
    st.markdown(js_code, unsafe_allow_html=True)

    footer.footer()


if __name__ == '__main__':
    main()
