import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="MicroDegree | Learn. Build. Grow.",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(
        135deg,
        #f7f9ff 0%,
        #eef2ff 55%,
        #ffffff 100%
    );
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* =========================================================
   HEADER
========================================================= */

.header {
    background: rgba(255,255,255,0.95);
    border: 1px solid #e7e9f5;
    border-radius: 18px;
    padding: 16px 24px;
    box-shadow: 0 8px 30px rgba(35,42,90,0.06);
    margin-bottom: 28px;
}

.logo {
    font-size: 25px;
    font-weight: 800;
    color: #173b8f;
}

.logo span {
    color: #5146e5;
}

/* =========================================================
   HERO SECTION
========================================================= */

.hero {
    background: linear-gradient(
        135deg,
        #ffffff 0%,
        #f1f4ff 100%
    );

    border: 1px solid #e4e8fa;
    border-radius: 26px;
    padding: 48px;

    box-shadow: 0 15px 45px rgba(42,52,120,0.08);

    min-height: 390px;
}

.badge {
    display: inline-block;

    background: #eceaff;
    color: #5146e5;

    padding: 8px 14px;

    border-radius: 30px;

    font-size: 13px;
    font-weight: 700;

    margin-bottom: 15px;
}

.hero h1 {
    font-size: 48px;
    line-height: 1.08;

    color: #13264f;

    margin: 0;

    font-weight: 800;
}

.hero h1 span {
    color: #5146e5;
}

.hero p {
    color: #64708d;

    font-size: 17px;

    line-height: 1.7;

    max-width: 620px;
}

/* =========================================================
   TECHNOLOGY CARDS
========================================================= */

.tech {
    background: white;

    border: 1px solid #e4e7f3;

    border-radius: 16px;

    padding: 18px;

    text-align: center;

    font-size: 28px;

    box-shadow: 0 7px 22px rgba(40,50,100,0.07);
}

/* =========================================================
   GENERAL CARDS
========================================================= */

.card {
    background: white;

    border: 1px solid #e7e9f3;

    border-radius: 18px;

    padding: 22px;

    height: 100%;

    box-shadow: 0 8px 24px rgba(30,40,90,0.06);
}

.card h3 {
    color: #172b58;

    margin-bottom: 7px;
}

.card p {
    color: #71809d;

    line-height: 1.55;
}

.icon {
    font-size: 30px;

    margin-bottom: 8px;
}

/* =========================================================
   SUCCESS SECTION
========================================================= */

.success {
    background: linear-gradient(
        135deg,
        #eefcf5,
        #f5f0ff,
        #fff8ea
    );

    border: 1px solid #d9e7f2;

    border-radius: 24px;

    padding: 35px;

    text-align: center;

    margin-bottom: 25px;
}

.success h1 {
    color: #163c89;

    margin: 5px 0;
}

.unlock {
    display: inline-block;

    background: white;

    padding: 13px 22px;

    border-radius: 14px;

    font-size: 19px;

    font-weight: 800;

    color: #5146e5;

    box-shadow: 0 8px 25px rgba(60,50,130,0.09);
}

/* =========================================================
   PROJECT CARDS
========================================================= */

.project {
    background: white;

    border: 1px solid #e5e8f2;

    border-radius: 18px;

    padding: 20px;

    min-height: 225px;

    box-shadow: 0 8px 25px rgba(35,45,100,0.06);
}

.project-icon {
    font-size: 38px;
}

.project h3 {
    color: #182c59;

    margin: 8px 0;
}

.project p {
    color: #6e7890;

    font-size: 14px;

    min-height: 43px;
}

.progress-bg {
    background: #edf0f7;

    height: 8px;

    border-radius: 10px;

    margin: 10px 0;
}

.progress-fill {
    background: linear-gradient(
        90deg,
        #5146e5,
        #7c3aed
    );

    height: 8px;

    border-radius: 10px;
}

/* =========================================================
   SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background: #101d3b;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* =========================================================
   BUTTONS
========================================================= */

.stButton > button {
    border-radius: 10px;

    font-weight: 700;

    border: none;

    min-height: 42px;
}

/* =========================================================
   RESPONSIVE
========================================================= */

@media (max-width: 768px) {

    .hero {
        padding: 28px 22px;
    }

    .hero h1 {
        font-size: 35px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "registered" not in st.session_state:
    st.session_state.registered = False

if "user" not in st.session_state:
    st.session_state.user = {}

if "selected_project" not in st.session_state:
    st.session_state.selected_project = None


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="header">

    <div class="logo">
        🎓 Micro<span>Degree</span>
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# REGISTRATION PAGE
# =========================================================

if not st.session_state.registered:

    left, right = st.columns(
        [1.35, 0.85],
        gap="large"
    )

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left:

        st.markdown("""
        <div class="hero">

            <div class="badge">
                🚀 CAREER-READY LEARNING
            </div>

            <h1>
                Learn Today,<br>
                <span>Build Tomorrow.</span>
            </h1>

            <p>
                Learn industry-ready skills through hands-on
                projects, practical learning and real-world
                technology.

                Start your journey toward your dream career.
            </p>

        </div>
        """, unsafe_allow_html=True)

        st.write("")

        c1, c2, c3, c4 = st.columns(4)

        features = [

            (
                "⚡",
                "Hands-on",
                "Projects"
            ),

            (
                "🏆",
                "Certificates",
                "Completion"
            ),

            (
                "👨‍🏫",
                "Expert",
                "Mentors"
            ),

            (
                "💼",
                "Career",
                "Support"
            )

        ]

        for col, (icon, title, sub) in zip(
            [c1, c2, c3, c4],
            features
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="card">

                        <div class="icon">
                            {icon}
                        </div>

                        <b>{title}</b>

                        <br>

                        <small>
                            {sub}
                        </small>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.write("")

        st.markdown(
            "### 🧑‍💻 Technologies You Can Learn"
        )

        tech_cols = st.columns(5)

        techs = [

            ("🐧", "Linux"),
            ("🔀", "Git"),
            ("🐳", "Docker"),
            ("☁️", "AWS"),
            ("☸️", "Kubernetes")

        ]

        for col, (icon, name) in zip(
            tech_cols,
            techs
        ):

            with col:

                st.markdown(
                    f"""
                    <div class="tech">

                        {icon}

                        <br>

                        <small>
                            {name}
                        </small>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


    # =====================================================
    # RIGHT SIDE - REGISTRATION
    # =====================================================

    with right:

        st.markdown(
            "### 🎓 Create Your Account"
        )

        st.caption(
            "Join MicroDegree and start your learning journey today!"
        )

        with st.form("registration_form"):

            full_name = st.text_input(
                "Full Name *",
                placeholder="Enter your full name"
            )

            email = st.text_input(
                "Email Address *",
                placeholder="you@example.com"
            )

            phone = st.text_input(
                "Phone Number *",
                placeholder="Enter phone number"
            )

            password = st.text_input(
                "Password *",
                type="password"
            )

            goal = st.selectbox(
                "Select Your Goal *",
                [
                    "DevOps Engineer",
                    "Cloud Engineer",
                    "Python Developer",
                    "Data Analyst",
                    "Full Stack Developer"
                ]
            )

            agree = st.checkbox(
                "I agree to the Terms & Conditions and Privacy Policy"
            )

            submitted = st.form_submit_button(
                "🚀 Register & Unlock Projects",
                use_container_width=True
            )


        # =================================================
        # FORM VALIDATION
        # =================================================

        if submitted:

            if not full_name:

                st.error(
                    "Please enter your full name."
                )

            elif not email:

                st.error(
                    "Please enter your email address."
                )

            elif "@" not in email:

                st.error(
                    "Please enter a valid email address."
                )

            elif not phone:

                st.error(
                    "Please enter your phone number."
                )

            elif not password:

                st.error(
                    "Please create a password."
                )

            elif not agree:

                st.error(
                    "Please accept the Terms & Conditions."
                )

            else:

                # Save user details
                st.session_state.user = {

                    "name": full_name,

                    "email": email,

                    "phone": phone,

                    "goal": goal

                }

                st.session_state.registered = True

                st.session_state.selected_project = None

                # Celebration
                st.balloons()

                st.rerun()


# =========================================================
# DASHBOARD
# =========================================================

else:

    # =====================================================
    # SIDEBAR
    # =====================================================

    with st.sidebar:

        st.markdown(
            "## 🎓 MicroDegree"
        )

        st.markdown("---")

        st.markdown(
            "🏠 **Dashboard**"
        )

        st.markdown(
            "📚 My Courses"
        )

        st.markdown(
            "💻 Projects"
        )

        st.markdown(
            "🏆 Certificates"
        )

        st.markdown(
            "👤 Profile"
        )

        st.markdown(
            "⚙️ Settings"
        )

        st.markdown("---")

        st.caption(
            "Small progress every day adds up to big results. 💜"
        )

        st.write("")

        if st.button(
            "Logout",
            use_container_width=True
        ):

            st.session_state.registered = False

            st.session_state.user = {}

            st.session_state.selected_project = None

            st.rerun()


    # =====================================================
    # USER INFORMATION
    # =====================================================

    name = st.session_state.user["name"]

    goal = st.session_state.user["goal"]


    # =====================================================
    # SUCCESS MESSAGE
    # =====================================================

    st.markdown(
        f"""
        <div class="success">

            <div style="font-size:42px;">
                🎉
            </div>

            <h1>
                Congratulations, {name}!
            </h1>

            <p>
                You have successfully registered
                with MicroDegree.
            </p>

            <div class="unlock">

                🔓 You've unlocked
                5 amazing projects!

            </div>

            <p style="margin-top:15px;">

                Your
                <b>{goal}</b>
                learning journey starts now. 🚀

            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # PROJECT SECTION
    # =====================================================

    st.markdown(
        "## 🚀 Your Unlocked Projects"
    )

    st.caption(
        "Build these projects to gain practical, job-ready experience."
    )


    projects = [

        (
            "🐧",
            "Linux Basics",
            "Learn Linux commands, users, permissions and file management.",
            20
        ),

        (
            "🔀",
            "Git & GitHub",
            "Practice version control, branching, merging and collaboration.",
            0
        ),

        (
            "🐳",
            "Docker",
            "Containerize applications and understand images and containers.",
            0
        ),

        (
            "☁️",
            "AWS",
            "Deploy and manage applications on cloud infrastructure.",
            0
        ),

        (
            "☸️",
            "Kubernetes",
            "Orchestrate and manage containers at scale.",
            0
        )

    ]


    # =====================================================
    # PROJECT CARDS
    # =====================================================

    cols = st.columns(5)


    for i, (
        icon,
        title,
        description,
        progress
    ) in enumerate(projects):

        with cols[i]:

            st.markdown(
                f"""
                <div class="project">

                    <div class="project-icon">
                        {icon}
                    </div>

                    <h3>
                        {title}
                    </h3>

                    <p>
                        {description}
                    </p>

                    <b>
                        {progress}% Complete
                    </b>

                    <div class="progress-bg">

                        <div
                            class="progress-fill"
                            style="width:{progress}%"
                        >
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


            if st.button(
                "Start Project →",
                key=f"project_{i}",
                use_container_width=True
            ):

                st.session_state.selected_project = title


    # =====================================================
    # SELECTED PROJECT
    # =====================================================

    if st.session_state.selected_project:

        project = st.session_state.selected_project

        st.write("")

        st.markdown(
            f"## 📘 {project}"
        )


        if project == "Linux Basics":

            st.info(
                """
                🎯 Start with Linux commands, files,
                directories, users and permissions.
                """
            )

            st.code(
                """
# Create a directory
mkdir devops-project

# Enter directory
cd devops-project

# Create a file
touch app.txt

# View files
ls

# Display current location
pwd
                """,
                language="bash"
            )


        elif project == "Git & GitHub":

            st.info(
                """
                🎯 Create a repository, commit code,
                create branches and push to GitHub.
                """
            )

            st.code(
                """
git init

git add .

git commit -m "Initial commit"

git branch -M main

git remote add origin <github-url>

git push -u origin main
                """,
                language="bash"
            )


        elif project == "Docker":

            st.info(
                """
                🎯 Build a Docker image, create a container
                and publish it to Docker Hub.
                """
            )

            st.code(
                """
docker build -t myapp .

docker images

docker run -d -p 8080:8080 myapp

docker ps

docker stop <container-id>
                """,
                language="bash"
            )


        elif project == "AWS":

            st.info(
                """
                🎯 Launch an AWS EC2 server and prepare
                it for application deployment.
                """
            )

            st.code(
                """
# Connect to EC2

ssh -i my-key.pem ubuntu@<EC2-IP>

# Update server

sudo apt update

# Install Docker

sudo apt install docker.io -y

# Check Docker

docker --version
                """,
                language="bash"
            )


        elif project == "Kubernetes":

            st.info(
                """
                🎯 Deploy your Docker application to
                Kubernetes using Pods, Deployments
                and Services.
                """
            )

            st.code(
                """
kubectl get nodes

kubectl get pods

kubectl get deployments

kubectl apply -f deployment.yaml

kubectl get services
                """,
                language="bash"
            )


        if st.button(
            "← Back to Dashboard"
        ):

            st.session_state.selected_project = None

            st.rerun()


    # =====================================================
    # QUICK LINKS
    # =====================================================

    st.write("")

    st.markdown(
        "## ⚡ Quick Links"
    )

    q1, q2, q3, q4 = st.columns(4)


    with q1:

        st.markdown(
            """
            <div class="card">

                <h3>
                    ▶️ Continue Learning
                </h3>

                <p>
                    Resume your last course.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with q2:

        st.markdown(
            """
            <div class="card">

                <h3>
                    🏆 Certificates
                </h3>

                <p>
                    Track your achievements.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with q3:

        st.markdown(
            """
            <div class="card">

                <h3>
                    ❓ Need Help?
                </h3>

                <p>
                    Get support from the team.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    with q4:

        st.markdown(
            """
            <div class="card">

                <h3>
                    👑 Upgrade Plan
                </h3>

                <p>
                    Unlock more learning features.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # FOOTER
    # =====================================================

    st.write("")

    st.markdown("---")

    st.caption(
        "© 2026 MicroDegree-style Learning Portal "
        "• Learn • Build • Grow 🚀"
    )