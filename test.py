import streamlit as st
from PIL import Image
import os

#------------------------------------------------------------------------------------------------
#login_page
#------------------------------------------------------------------------------------------------

def login_page():
    st.title("Login to Our Platform")
    st.write("Please enter your credentials to access the platform.")
    
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    if st.button("Login"):
        if username == "p" and password == "p":
            st.session_state.logged_in = True
            st.success("Successfully logged in!")
        else:
            st.error("Invalid username or password.")

#------------------------------------------------------------------------------------------------
#parasitic_home_page
#------------------------------------------------------------------------------------------------

def parasitic_home_page():
    st.title("Parasitic Platform")
    st.subheader("Introduction and overview")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Biological Parasite")
        st.write("""
        A parasite is an organism that lives on or inside another organism (called the host) and benefits at the host's expense. This relationship often harms the host. Parasites come in many forms, including:
        - Protozoa (microscopic single-celled organisms)
        - Helminths (parasitic worms)
        - Ectoparasites like lice or ticks
        - Fungi and bacteria that can act in parasitic roles
                 
        Parasites have evolved various adaptations to exploit their hosts and may have complex life cycles involving more than one host.
                 """)

    with col2:
        st.header("Key Areas of Focus")
        st.subheader("**Evolutionary Arms Race**")
        st.write("""
        Parasite-host interactions are emblematic of a continuous coevolutionary struggle. Hosts evolve defense mechanisms, such as enhanced immune responses, while parasites concurrently develop sophisticated strategies to circumvent these defenses, including antigenic variation and immune modulation. This reciprocal adaptation drives biodiversity and complexity within ecosystems.
                 """)
        st.subheader("**Mechanisms of Immune Evasion**")
        st.write("""
        Many parasites, including protozoans and helminths, have evolved mechanisms to avoid detection or neutralize host immune responses. For example, some parasites secrete molecules that mimic host proteins, thereby blurring the line between self and non-self, which can lead to chronic infections. Understanding these mechanisms provides insights into potential therapeutic targets for controlling parasitic diseases.
                 """)
        st.subheader("Ecological Consequences")
        st.write("""
        Beyond the individual level, parasites can influence host population dynamics and community structures. In some ecosystems, parasites regulate host populations, thereby maintaining species diversity and ecological balance. Conversely, parasite outbreaks can lead to significant morbidity and mortality in host populations, potentially triggering cascading effects throughout the ecosystem.
                 """)
        st.subheader("Disease Ecology and Public Health")
        st.write("""
        The study of parasite-host interactions is crucial in the context of emerging infectious diseases. Changes in environmental conditions, global travel, and human encroachment into wildlife habitats can alter parasite transmission dynamics. Research in this field is vital for predicting and mitigating the impact of parasitic diseases on public health.
                 """)

#------------------------------------------------------------------------------------------------
#parasitic_lecture_page
#------------------------------------------------------------------------------------------------

def parasitic_lecture_page():
    st.title("Parasitic Lecture: *Enterobius Vermicularis*")
    
    st.subheader("Chapter 1: Taxonomy and Classification")
    st.write("""Enterobius vermicularis, commonly known as the human pinworm, is a parasitic nematode belonging to the phylum Nematoda. It is classified under the class Secernentea, order Oxyurida, and family Oxyuridae. This parasite is a highly specialized obligate human endoparasite, primarily colonizing the large intestine. The species is widely distributed and is the most prevalent helminthic infection in humans, particularly affecting children in temperate and tropical regions.""")
    
    st.subheader("Chapter 2: Morphology")
    st.write("""The adult E. vermicularis exhibits sexual dimorphism, with females being significantly larger than males. The female worm measures approximately 8–13 mm in length and 0.3–0.5 mm in width, while the male is smaller, ranging from 2–5 mm in length and 0.1–0.2 mm in width. The cuticle of the worm features characteristic transverse striations, and the anterior end possesses cephalic alae, which facilitate attachment to the intestinal mucosa. The male has a curved posterior end with a single copulatory spicule, while the female has a long, sharply pointed tail, which contributes to its common name, "pinworm." The eggs of E. vermicularis are oval and asymmetrical, measuring 50–60 µm in length and 20–30 µm in width. The shell is smooth and translucent, with a fully developed larva visible inside when freshly excreted.""")

    st.subheader("Chapter 3: Life Cycle")
    st.write("""The life cycle of E. vermicularis is direct, requiring no intermediate host, and is completed within the human gastrointestinal tract. Infection occurs via ingestion of embryonated eggs, which hatch in the duodenum or jejunum. The released larvae migrate to the cecum and colon, where they mature into adults over a period of 2–4 weeks. After copulation, the male worm dies, while the gravid female migrates to the perianal region during the night to deposit thousands of eggs. The eggs become infective within 4–6 hours, leading to autoinfection through hand-to-mouth transmission when the host scratches the perianal area. Indirect transmission occurs through contaminated fomites, while airborne eggs may lead to inhalation-based infections. Retroinfection, in which larvae hatch and migrate back into the rectum, has also been reported in some cases.""")

    st.subheader("Chapter 4: Epidemiology")
    st.write("""Enterobius vermicularis is a globally distributed parasite, with infections occurring in both developed and developing regions. It is most prevalent in children aged 5–10 years and in individuals living in crowded conditions such as schools, daycare centers, and institutional settings. Studies have reported infection rates as high as 30–50% in school-aged children, particularly in temperate climates. The primary mode of transmission is the fecal-oral route, with eggs spreading through direct hand contamination, contaminated food, clothing, and bedding. Airborne transmission is possible when eggs become aerosolized, and retroinfection may contribute to persistent infections. Reinfection is common due to the parasite’s high environmental resistance and its ability to persist on surfaces for up to three weeks.""")

    st.subheader("Chapter 5: Pathogenesis and Clinical Manifestations")
    st.write("""The pathogenesis of E. vermicularis is primarily associated with mechanical irritation, immune response, and secondary bacterial infections. The adult worms inhabit the cecum, appendix, and colon, where they may cause mild mucosal inflammation. The migration of gravid females to the perianal region induces intense pruritus, leading to scratching, sleep disturbances, and behavioral changes in children. In some cases, heavy infections can result in weight loss, abdominal pain, and gastrointestinal discomfort. Secondary bacterial infections may arise from excoriated perianal skin. In rare instances, the parasite has been implicated in appendicitis and ectopic enterobiasis, where worms invade the female reproductive tract, potentially leading to pelvic inflammatory disease (PID).""")

    st.subheader("Chapter 6: Diagnosis")
    st.write("""The primary diagnostic method for E. vermicularis infection is the adhesive cellophane tape test (Graham’s method), which involves applying transparent tape to the perianal skin in the morning before bathing. The tape is then examined microscopically for the presence of eggs. This method has high sensitivity when performed on multiple consecutive days. Stool examination is generally not useful, as eggs are rarely excreted in feces. Direct visualization of adult worms in the perianal area, especially at night, can provide confirmatory evidence. Molecular diagnostic tools such as polymerase chain reaction (PCR) have been explored for more sensitive detection, though they are not widely used in routine clinical settings.""")
    
    st.subheader("Chapter 7: Treatment and Prevention")
    st.write("""The treatment of E. vermicularis involves the administration of anthelmintic agents such as mebendazole, albendazole, and pyrantel pamoate. A single oral dose is typically followed by a second dose two weeks later to prevent reinfection. Since E. vermicularis spreads rapidly within households and institutions, simultaneous treatment of all household members is recommended. Preventive measures include maintaining strict personal hygiene, frequent handwashing, keeping fingernails short, and avoiding nail-biting or thumb-sucking. Environmental control strategies involve washing bedding and undergarments in hot water, vacuuming surfaces, and disinfecting household items to eliminate residual eggs.""")
    
    st.subheader("Chapter 8: Research and Emerging Trends")
    st.write("""Recent research has focused on improving diagnostic techniques through artificial intelligence and machine learning-based image recognition for automated detection of E. vermicularis eggs in microscopic images. Molecular diagnostic approaches, including PCR and loop-mediated isothermal amplification (LAMP), are being explored for enhanced sensitivity. Additionally, studies on drug resistance and alternative therapeutic agents are ongoing to improve treatment efficacy. The development of better epidemiological monitoring tools is crucial for controlling the prevalence and reinfection rates of this highly transmissible parasite.""")

    st.subheader("Chapter 9: Conclusion")
    st.write("""Enterobius vermicularis remains a widespread parasitic infection with significant public health implications, particularly in children. Although rarely associated with severe complications, the parasite causes considerable discomfort and disrupts quality of life through its highly infectious nature. Effective management strategies, including pharmacological treatment, environmental decontamination, and personal hygiene practices, are critical in reducing transmission. Advances in diagnostic technologies and epidemiological surveillance will play a crucial role in improving control measures for E. vermicularis infections worldwide.""")

#------------------------------------------------------------------------------------------------
#parasitic_image_viewer_page
#------------------------------------------------------------------------------------------------

def parasitic_image_viewer_page():
    st.title("Parasite Image Viewer")
    st.write("This app displays images from a local folder in a grid layout.")

    #--------------------------------------------------------------------------------------------
    #folder = "E:/P Works/My Projects/Project - ทุน ศ สูง มข/web_component/ev-web"
    folder = "ev-web"
    #--------------------------------------------------------------------------------------------

    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tif')):
            filepath = os.path.join(folder, filename)
            try:
                image = Image.open(filepath)
                images.append((filename, image))
            except Exception as e:
                st.error(f"Error loading image {filename}: {e}")
    if not os.path.exists(folder):
        st.error(f"The folder '{folder}' does not exist. Please create it and add some images.")
        return

    if images:
        cols_per_row = 5
        for i in range(0, len(images), cols_per_row):
            cols = st.columns(cols_per_row)
            for col, (filename, image) in zip(cols, images[i:i+cols_per_row]):
                #col.image(image, caption=filename, use_column_width=True)
                col.image(image, caption=filename, use_container_width=True)
    else:
        st.info("No images found in the folder.")

#------------------------------------------------------------------------------------------------
#parasitic_examination_page
#------------------------------------------------------------------------------------------------

def parasitic_examination_page():
    st.title("Parasitic Examination")
    st.write("This is the exam page. Good luck!")
    
    st.subheader("Sample Question: true or false")
    st.write("1. Enterobius vermicularis requires an intermediate host to complete its life cycle.")
    answer = st.text_input("Your Answer", placeholder="Type your answer here...")
    if st.button("Submit Answer"):
        if answer.strip().lower() == "False":
            st.success("Correct Answer!")
        elif answer.strip().lower() == "false":
            st.success("Correct Answer!")
        else:
            st.error("Incorrect Answer. Try Again!")

#------------------------------------------------------------------------------------------------
#parasitic_detection_page
#------------------------------------------------------------------------------------------------

import cv2
import numpy as np
import tensorflow as tf

def parasitic_detection_page():
    st.title("Parasitic Detection")
    st.subheader("Upload & View Image")
    st.write("Upload an image and view it below.")

    #--------------------------------------------------------------------------------------------
    #model_path = "E:/P Works/My Projects/Project - ทุน ศ สูง มข/web_component/model/aug_img_cnn.h5"
    model_path = "model/aug_img_cnn.h5"
    #--------------------------------------------------------------------------------------------

    model = tf.keras.models.load_model(model_path, custom_objects={'mse': tf.keras.losses.MeanSquaredError()})

    def boxlocation(img_c, box_size):
        non_zero_points = np.argwhere(img_c > 0)
        if non_zero_points.size == 0:
            return None

        y_min, x_min = np.min(non_zero_points, axis=0)
        y_max, x_max = np.max(non_zero_points, axis=0)

        return [y_min - box_size, y_max + box_size, x_min - box_size, x_max + box_size]

    def drawbox(img, label, a, b, c, d, box_size):
        image = cv2.rectangle(img, (c, a), (d, b), (0, 255, 0), 2)
        image = cv2.putText(image, label, (c + box_size, a - 10), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 1)
        return image

    def objectdet(img):
        img = cv2.resize(img, (img.shape[1] // 1, img.shape[0] // 1), interpolation=cv2.INTER_AREA)
        
        box_size_y, box_size_x = 200, 200
        step_size = 50
        img_output = np.array(img)
        img_cont = np.zeros((img_output.shape[0], img_output.shape[1]), dtype=np.uint8)
        result = 0

        for i in range(0, img_output.shape[0] - box_size_y, step_size):
            for j in range(0, img_output.shape[1] - box_size_x, step_size):
                img_patch = img_output[i:i + box_size_y, j:j + box_size_x]
                img_patch = cv2.resize(img_patch, (128, 128), interpolation=cv2.INTER_AREA)
                img_patch = np.expand_dims(img_patch, axis=0)

                y_outp = model.predict(img_patch, verbose=0)

                if result < y_outp[0][1] and y_outp[0][1] > 0.95:
                    result = y_outp[0][1]
                    img_cont[i + (box_size_y // 2), j + (box_size_x // 2)] = int(y_outp[0][1] * 255)

        if result != 0:
            label = f"ev: {result:.2f}"
            boxlocat = boxlocation(img_cont, box_size_x // 2)
            if boxlocat:
                img_output = drawbox(img, label, *boxlocat, box_size_x // 2)

        return img_output

    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg", "tif"])
    if uploaded_file is not None:
        try:
            image = np.array(Image.open(uploaded_file))
            if image.ndim == 2:
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            output_img = objectdet(image)
            st.image(output_img, caption="Processed Image", use_column_width=True)

        except Exception as e:
            st.error(f"Error loading image: {e}")
            
#------------------------------------------------------------------------------------------------
#about_page
#------------------------------------------------------------------------------------------------

def about_page():
    st.title("About")
    st.write("""**Parasitic Platform** is built using [Streamlit](https://streamlit.io/) to deliver a stunning UI/UX experience.""")

#------------------------------------------------------------------------------------------------
#main function
#------------------------------------------------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
else:
    st.sidebar.title("Platform Navigation")
    selected_page = st.sidebar.radio(
        "Go to", 
        ("Parasitic Home", "Parasitic Lecture", "Parasitic Image Viewer", "Parasitic Examination", "Parasitic Detection", "About"))
    
    if selected_page == "Parasitic Home":
        parasitic_home_page()
    elif selected_page == "Parasitic Lecture":
        parasitic_lecture_page()
    elif selected_page == "Parasitic Image Viewer":
        parasitic_image_viewer_page()
    elif selected_page == "Parasitic Examination":
        parasitic_examination_page()
    elif selected_page == "Parasitic Detection":
        parasitic_detection_page()
    elif selected_page == "About":
        about_page()
    
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
