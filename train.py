import streamlit as st

# Define yoga poses with their pre- and post-asana precautions
yoga_poses = {
    "Child’s Pose (Shishuasana)": {
        "pre": [
            "Avoid if you have knee injuries, severe back pain, or late-stage pregnancy.",
            "High blood pressure patients should avoid keeping their head too low.",
            "Move into the pose slowly if you have dizziness or vertigo.",
            "Avoid if you have diarrhea or digestive issues.",
            "Modify by placing a cushion under the ankles if you have ankle injuries.",
            "If you have shoulder pain, keep your arms by your sides instead of stretching forward."
        ],
        "post": [
            "Avoid intense backbends immediately after.",
            "Don’t stand up suddenly if you feel dizzy.",
            "Wait at least 15-20 minutes before eating a full meal.",
            "Gently stretch your legs if you feel numbness after holding the pose."
        ]
    },
    "Bound Angle Pose (Baddha Konasana)": {
        "pre": [
            "If you have a hip injury, avoid pressing the knees too hard.",
            "Sit with support under the hips if you have lower back pain.",
            "Avoid if you've had recent groin surgery.",
            "Use a cushion under the hips if you have sciatica.",
            "Avoid if you have severe arthritis in the knees.",
            "Keep the spine neutral if you have herniated discs."
        ],
        "post": [
            "Avoid running or jumping immediately after the pose.",
            "Do gentle counterposes if you feel strain in the hips.",
            "Stretch your legs straight before sitting cross-legged if you feel stiffness.",
            "Massage your feet if you feel tingling or numbness."
        ]
    },
    "Cat-Cow Pose (Marjaryasana-Bitilasana)": {
        "pre": [
            "If you have wrist or hand injuries, modify the pose by practicing on your forearms or using a folded towel for extra support.",
            "Those with chronic neck pain should avoid tilting the head too far back during the cow phase; keep movements gentle and within a comfortable range.",
            "If you have severe back issues or recent spinal surgery, perform the transitions slowly or consult a healthcare provider before attempting this pose.",
            "Pregnant practitioners should take extra care and use modifications as needed; if in doubt, consult with a professional.",
            "If you experience stiffness or discomfort in the knees or hips, consider using a cushion or reducing the range of motion."
        ],
        "post": [
            "Avoid quickly transitioning into intense backbends or other strenuous poses immediately afterward; allow your spine to settle back into a neutral position.",
            "Stand up slowly, especially if you feel any lightheadedness or discomfort after the fluid motion.",
            "If your wrists or back feel strained, take a few moments to rest in a neutral seated or lying position before moving on to other exercises.",
            "Give your body time to adjust after the continuous movement by pausing for a brief cool-down period."
        ]
    },
    "Downward Facing Dog Pose (Adho Mukha Svanasana)": {
        "pre": [
            "If you experience wrist pain or have a history of wrist injuries, consider modifying the pose by using props (like blocks) or practicing on your forearms to lessen the strain.",
            "Those with shoulder or upper back issues should ease into the pose and avoid overextending their arms.",
            "If you have chronic back or neck pain, practice a gentle version of the pose or consult a professional before attempting the full expression.",
            "Pregnant practitioners should modify the pose to reduce pressure on the abdomen and ensure a safe range of motion.",
            "If you have tight calves or hamstrings, bend your knees slightly to prevent excessive strain on your lower legs.",
            "Individuals with high blood pressure or a tendency toward dizziness should be cautious with the inversion; avoid holding the pose too long or lowering your head excessively."
        ],
        "post": [
            "Do not stand up or change positions abruptly after exiting the pose. Transition slowly to a neutral position to avoid lightheadedness.",
            "Refrain from performing vigorous or deep forward bends immediately after, as your muscles may need time to adjust.",
            "If you experience numbness or discomfort in your wrists post-pose, gently shake them out and rest before proceeding with other movements.",
            "Allow a brief period for your body to relax and recover, especially if the pose has put significant strain on your calves or hamstrings."
        ]
    },
    "Mountain Pose (Tadasana)": {
        "pre": [
            "If you have foot, ankle, or knee issues, ensure proper weight distribution. Using a wall or support can help maintain balance.",
            "Individuals with chronic back pain or spinal concerns should engage their core muscles gently to support an upright alignment.",
            "Those prone to dizziness or instability may practice near a stable surface or modify the pose to reduce the risk of falls.",
            "If you experience joint pain or have hypermobility, focus on controlled movements and maintain a slight muscle engagement to prevent overextension.",
            "Pregnant practitioners should adapt their stance to a comfortable width and consider additional support if needed."
        ],
        "post": [
            "Avoid abrupt movements or rapid transitions from the pose to prevent any lightheadedness or imbalance.",
            "If you notice fatigue or discomfort in the legs, feet, or back after holding the pose, take a few moments to gently stretch or relax.",
            "When moving into subsequent poses, ensure your posture is realigned and your muscles are ready for the next movement.",
            "Should any discomfort arise, allow time for a brief seated rest or perform gentle stretches before continuing with your practice."
        ]
    },
    "Angle Pose (Utthita Parsvakonasana)": {
        "pre": [
            "If you have knee or ankle issues, ensure your front knee is aligned and not overextended; consider using a support or modifying the depth of the bend.",
            "For those with tight hips or groin muscles, ease gradually into the pose to prevent overstretching or strain.",
            "If you experience lower back discomfort or have a history of spinal issues, engage your core and avoid forcing a deep twist.",
            "If your shoulders feel strained or injured, modify the arm position by reducing the overhead reach.",
            "Pregnant practitioners should maintain a comfortable range of motion and avoid deep twists or overly intense stretches during the pose."
        ],
        "post": [
            "Exit the pose gradually to avoid sudden strain on your knees, hips, or lower back.",
            "If you feel any lingering discomfort or tightness in the hips, back, or legs, take a moment in a neutral stance before moving on.",
            "Refrain from engaging in further intense twisting or lateral bending immediately afterward; allow your muscles time to relax and recover.",
            "Should any joint or muscle tension persist, perform gentle stretches or rest in a seated position before resuming your practice."
        ]
    }
}

medical_conditions = [
    "High blood pressure", "Dizziness", "Vertigo", "Digestive issues", "Sciatica",
    "Arthritis", "Herniated discs", "Chronic neck pain", "Spinal issues", "Hyper-mobility"
]

injuries = [
    "Knee injuries", "Back pain (severe or chronic)", "Ankle injuries", "Shoulder pain or injuries",
    "Hip injury", "Groin surgery (recent)", "Wrist or hand injuries", "Spinal surgery (recent)",
    "Foot injuries", "Calf or hamstring strain"
]


st.title("Yoga Pose Precautions")
# Display only the yoga image in the main panel initially
st.image("download.jpeg", caption="Yoga Pose", use_container_width=True)

# Sidebar for user input (all inputs including pose selection, medical condition, and injury)
st.sidebar.header("User Details and Pose Selection")
age = st.sidebar.text_input("Age")
weight = st.sidebar.text_input("Weight (kg)")
flexibility = st.sidebar.selectbox("Flexibility Level", ["Low", "Medium", "High"])
selected_pose = st.sidebar.selectbox("Select Your Yoga Pose", list(yoga_poses.keys()))
selected_condition = st.sidebar.selectbox("Select Medical Condition", ["None"] + medical_conditions)
selected_injury = st.sidebar.selectbox("Select Injury", ["None"] + injuries)

# When the user clicks Submit, update the main panel with the prediction and precautions
if st.sidebar.button("Submit"):
    # Simple risk prediction logic
    risk = "Safe"  # default risk level
    if selected_condition != "None" or selected_injury != "None":
        risk = "Caution"
    if selected_condition != "None" and selected_injury != "None":
        risk = "Avoid"
    
    st.subheader("Risk Prediction Result")
    st.write(f"**Predicted Risk Level:** {risk}")
    st.write("Based on your input, please review the following precautions:")
    
    st.subheader(f"Precautions for {selected_pose}")
    st.write("### Pre-Asana Precautions:")
    for precaution in yoga_poses[selected_pose]["pre"]:
        st.write(f"- {precaution}")
    
    st.write("### Post-Asana Precautions:")
    for precaution in yoga_poses[selected_pose]["post"]:
        st.write(f"- {precaution}")
