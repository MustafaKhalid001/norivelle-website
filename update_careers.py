import re

with open('careers.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_form = """    <section id="application-form" style="padding: 5rem 0; background-color: var(--bg-color);">
        <div class="container">
            <div class="section-header" style="text-align: center; margin-bottom: 40px;">
                <h4 style="color: var(--primary); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; font-size: 0.9rem;">Ready to make an impact?</h4>
                <h2 style="font-size: 2.5rem; margin-bottom: 15px;">Apply Now</h2>
                <p style="color: var(--text-muted);">Fill out the form below to submit your application. We're excited to hear from you!</p>
            </div>

            <div class="multi-step-form-container" style="background-color: var(--bg-secondary); border-radius: 12px; padding: 40px; box-shadow: var(--shadow); max-width: 900px; margin: 0 auto; border: 1px solid var(--border-color);">
                
                <style>
                    @media (max-width: 768px) {
                        .step-grid-2 { grid-template-columns: 1fr !important; }
                        .form-progress { flex-direction: column; gap: 20px; }
                        .form-progress .connecting-line { display: none; }
                        .step-indicator { display: flex; align-items: center; text-align: left !important; gap: 15px; }
                        .step-indicator .step-circle { margin: 0 !important; }
                    }
                    .file-upload-box:hover {
                        border-color: var(--primary) !important;
                        background-color: rgba(139, 92, 246, 0.05) !important;
                    }
                </style>

                <!-- Progress Bar -->
                <div class="form-progress" style="display: flex; justify-content: space-between; position: relative; margin-bottom: 40px;">
                    <div class="connecting-line" style="position: absolute; top: 15px; left: 0; right: 0; height: 2px; background-color: var(--border-color); z-index: 1;"></div>
                    
                    <div class="step-indicator active" data-step="1" style="position: relative; z-index: 2; text-align: center; background: var(--bg-secondary); padding: 0 10px;">
                        <div class="step-circle" style="width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--primary); color: var(--primary); background: var(--bg-secondary); line-height: 28px; margin: 0 auto 10px; font-weight: bold; transition: all 0.3s ease;">1</div>
                        <div class="step-label" style="font-size: 0.8rem; font-weight: 600; color: var(--primary); text-transform: uppercase; transition: all 0.3s ease;">Personal<br>Info</div>
                    </div>
                    <div class="step-indicator" data-step="2" style="position: relative; z-index: 2; text-align: center; background: var(--bg-secondary); padding: 0 10px;">
                        <div class="step-circle" style="width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--text-muted); color: var(--text-muted); background: var(--bg-secondary); line-height: 28px; margin: 0 auto 10px; font-weight: bold; transition: all 0.3s ease;">2</div>
                        <div class="step-label" style="font-size: 0.8rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; transition: all 0.3s ease;">Experience</div>
                    </div>
                    <div class="step-indicator" data-step="3" style="position: relative; z-index: 2; text-align: center; background: var(--bg-secondary); padding: 0 10px;">
                        <div class="step-circle" style="width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--text-muted); color: var(--text-muted); background: var(--bg-secondary); line-height: 28px; margin: 0 auto 10px; font-weight: bold; transition: all 0.3s ease;">3</div>
                        <div class="step-label" style="font-size: 0.8rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; transition: all 0.3s ease;">Education</div>
                    </div>
                    <div class="step-indicator" data-step="4" style="position: relative; z-index: 2; text-align: center; background: var(--bg-secondary); padding: 0 10px;">
                        <div class="step-circle" style="width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--text-muted); color: var(--text-muted); background: var(--bg-secondary); line-height: 28px; margin: 0 auto 10px; font-weight: bold; transition: all 0.3s ease;">4</div>
                        <div class="step-label" style="font-size: 0.8rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; transition: all 0.3s ease;">Final<br>Uploads</div>
                    </div>
                </div>

                <!-- Form Content -->
                <form id="career-application-form">
                    <!-- Step 1 Content -->
                    <div class="form-step active" id="step-1">
                        <div class="form-group" style="margin-bottom: 20px;">
                            <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Application Type <span style="color: var(--primary);">*</span></label>
                            <div style="display: flex; gap: 20px;">
                                <label style="display: flex; align-items: center; gap: 8px; cursor: pointer; color: var(--text-color);">
                                    <input type="radio" name="application_type" value="Job" required checked style="accent-color: var(--primary); width: 18px; height: 18px;"> Job
                                </label>
                                <label style="display: flex; align-items: center; gap: 8px; cursor: pointer; color: var(--text-color);">
                                    <input type="radio" name="application_type" value="Internship" required style="accent-color: var(--primary); width: 18px; height: 18px;"> Internship
                                </label>
                            </div>
                        </div>

                        <div class="step-grid-2" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Full Name <span style="color: var(--primary);">*</span></label>
                                <input type="text" id="app_name" placeholder="Please enter your full name" required style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;">
                            </div>
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Email Address <span style="color: var(--primary);">*</span></label>
                                <input type="email" id="app_email" placeholder="Please enter your email address" required style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;">
                                <small id="email_error" style="color: red; display: none; margin-top: 5px;">Please enter a valid email address.</small>
                            </div>
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Phone Number <span style="color: var(--primary);">*</span></label>
                                <input type="tel" id="app_phone" placeholder="Please enter your contact number" required style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;">
                                <small id="phone_error" style="color: red; display: none; margin-top: 5px;">Please enter a valid phone number (min 10 digits).</small>
                            </div>
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Address <span style="color: var(--primary);">*</span></label>
                                <input type="text" id="app_address" placeholder="Enter your Full Address" required style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;">
                            </div>
                        </div>
                        <div style="margin-top: 30px;">
                            <button type="button" class="btn btn-primary next-step" style="padding: 12px 35px; border-radius: 8px; font-weight: bold; background-color: var(--primary); color: white; border: none; cursor: pointer; transition: all 0.3s ease;" onmouseover="this.style.boxShadow='0 5px 15px rgba(139, 92, 246, 0.4)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.boxShadow='none'; this.style.transform='translateY(0)';">NEXT</button>
                        </div>
                    </div>

                    <!-- Step 2 Content -->
                    <div class="form-step" id="step-2" style="display: none;">
                        <div style="display: grid; grid-template-columns: 1fr; gap: 20px;">
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Current/Most Recent Job Title</label>
                                <input type="text" id="app_job_title" placeholder="e.g. Senior SEO Specialist" style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;">
                            </div>
                            <div class="step-grid-2" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                                <div class="form-group">
                                    <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Years of Experience</label>
                                    <input type="number" id="app_experience" placeholder="e.g. 5" style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;">
                                </div>
                                <div class="form-group">
                                    <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Expected Salary (PKR/USD) <span style="color: var(--primary);">*</span></label>
                                    <input type="number" id="app_salary" placeholder="e.g. 150000" required style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;">
                                </div>
                            </div>
                        </div>
                        <div style="margin-top: 30px; display: flex; gap: 15px;">
                            <button type="button" class="btn btn-outline prev-step" style="padding: 12px 35px; border-radius: 8px; font-weight: bold; background-color: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; transition: all 0.3s ease;" onmouseover="this.style.backgroundColor='var(--primary)'; this.style.color='white';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='var(--primary)';">BACK</button>
                            <button type="button" class="btn btn-primary next-step" style="padding: 12px 35px; border-radius: 8px; font-weight: bold; background-color: var(--primary); color: white; border: none; cursor: pointer; transition: all 0.3s ease;" onmouseover="this.style.boxShadow='0 5px 15px rgba(139, 92, 246, 0.4)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.boxShadow='none'; this.style.transform='translateY(0)';">NEXT</button>
                        </div>
                    </div>

                    <!-- Step 3 Content -->
                    <div class="form-step" id="step-3" style="display: none;">
                        <div style="display: grid; grid-template-columns: 1fr; gap: 20px;">
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Highest Education Level</label>
                                <input type="text" id="app_education" placeholder="e.g. Bachelor's in Computer Science" style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;">
                            </div>
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Certifications / Portfolio Link</label>
                                <input type="text" id="app_certifications" placeholder="List any relevant certifications or link to portfolio" style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;">
                            </div>
                        </div>
                        <div style="margin-top: 30px; display: flex; gap: 15px;">
                            <button type="button" class="btn btn-outline prev-step" style="padding: 12px 35px; border-radius: 8px; font-weight: bold; background-color: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; transition: all 0.3s ease;" onmouseover="this.style.backgroundColor='var(--primary)'; this.style.color='white';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='var(--primary)';">BACK</button>
                            <button type="button" class="btn btn-primary next-step" style="padding: 12px 35px; border-radius: 8px; font-weight: bold; background-color: var(--primary); color: white; border: none; cursor: pointer; transition: all 0.3s ease;" onmouseover="this.style.boxShadow='0 5px 15px rgba(139, 92, 246, 0.4)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.boxShadow='none'; this.style.transform='translateY(0)';">NEXT</button>
                        </div>
                    </div>

                    <!-- Step 4 Content -->
                    <div class="form-step" id="step-4" style="display: none;">
                        <div style="display: grid; grid-template-columns: 1fr; gap: 30px;">
                            
                            <!-- Resume -->
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Resume / CV <span style="color: var(--primary);">*</span></label>
                                <div class="file-upload-box" id="resume-box" onclick="document.getElementById('file_resume').click()" style="border: 2px dashed var(--border-color); border-radius: 8px; padding: 20px; text-align: center; cursor: pointer; transition: all 0.3s ease; background: var(--bg-color);">
                                    <i class="fa-solid fa-cloud-arrow-up" style="font-size: 2rem; color: var(--primary); margin-bottom: 10px;"></i>
                                    <p style="margin: 0; color: var(--text-muted);">Drag & Drop your Resume here or <span style="color: var(--primary); font-weight: bold;">Click to Upload</span></p>
                                    <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 5px;">(Word or PDF)</p>
                                    <input type="file" id="file_resume" accept=".pdf,.doc,.docx" style="display: none;">
                                    <p class="file-name-display" id="name_resume" style="margin-top: 10px; font-weight: bold; color: var(--primary); display: none;"></p>
                                </div>
                                <div style="text-align: center; color: var(--text-muted); margin: 10px 0;">- OR -</div>
                                <input type="text" id="link_resume" placeholder="Provide a link (Google Drive, LinkedIn, etc.)" style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none;">
                            </div>

                            <!-- Cover Letter -->
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">Cover Letter</label>
                                <div class="file-upload-box" id="cover-box" onclick="document.getElementById('file_cover').click()" style="border: 2px dashed var(--border-color); border-radius: 8px; padding: 20px; text-align: center; cursor: pointer; transition: all 0.3s ease; background: var(--bg-color);">
                                    <i class="fa-solid fa-cloud-arrow-up" style="font-size: 2rem; color: var(--primary); margin-bottom: 10px;"></i>
                                    <p style="margin: 0; color: var(--text-muted);">Drag & Drop your Cover Letter here or <span style="color: var(--primary); font-weight: bold;">Click to Upload</span></p>
                                    <input type="file" id="file_cover" accept=".pdf,.doc,.docx" style="display: none;">
                                    <p class="file-name-display" id="name_cover" style="margin-top: 10px; font-weight: bold; color: var(--primary); display: none;"></p>
                                </div>
                                <div style="text-align: center; color: var(--text-muted); margin: 10px 0;">- OR -</div>
                                <textarea id="link_cover" placeholder="Or type your cover letter here..." rows="3" style="width: 100%; padding: 12px 15px; border: 1px solid var(--border-color); border-radius: 8px; background: var(--bg-color); color: var(--text-color); outline: none; transition: all 0.3s ease;"></textarea>
                            </div>

                            <!-- CNIC / B-Form -->
                            <div class="form-group">
                                <label style="display: block; margin-bottom: 8px; font-weight: 600; color: var(--text-color);">CNIC / B-Form (Scanned Copy) <span style="color: var(--primary);">*</span></label>
                                <div class="file-upload-box" id="cnic-box" onclick="document.getElementById('file_cnic').click()" style="border: 2px dashed var(--border-color); border-radius: 8px; padding: 20px; text-align: center; cursor: pointer; transition: all 0.3s ease; background: var(--bg-color);">
                                    <i class="fa-solid fa-id-card" style="font-size: 2rem; color: var(--primary); margin-bottom: 10px;"></i>
                                    <p style="margin: 0; color: var(--text-muted);">Drag & Drop your CNIC / B-Form here or <span style="color: var(--primary); font-weight: bold;">Click to Upload</span></p>
                                    <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 5px;">(Image or PDF)</p>
                                    <input type="file" id="file_cnic" accept=".pdf,.jpg,.jpeg,.png" style="display: none;">
                                    <p class="file-name-display" id="name_cnic" style="margin-top: 10px; font-weight: bold; color: var(--primary); display: none;"></p>
                                </div>
                            </div>
                        </div>

                        <!-- Submit Button Area -->
                        <div style="margin-top: 30px; display: flex; gap: 15px; align-items: center;">
                            <button type="button" class="btn btn-outline prev-step" style="padding: 12px 35px; border-radius: 8px; font-weight: bold; background-color: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; transition: all 0.3s ease;" onmouseover="this.style.backgroundColor='var(--primary)'; this.style.color='white';" onmouseout="this.style.backgroundColor='transparent'; this.style.color='var(--primary)';">BACK</button>
                            <button type="submit" id="submit_btn" class="btn btn-primary" style="padding: 12px 35px; border-radius: 8px; font-weight: bold; background-color: var(--primary); color: white; border: none; cursor: pointer; transition: all 0.3s ease;" onmouseover="this.style.boxShadow='0 5px 15px rgba(139, 92, 246, 0.4)'; this.style.transform='translateY(-2px)';" onmouseout="this.style.boxShadow='none'; this.style.transform='translateY(0)';">SUBMIT APPLICATION</button>
                            <span id="submit_msg" style="color: var(--primary); font-weight: bold; display: none; margin-left: 15px;">Processing...</span>
                        </div>
                    </div>
                </form>
            </div>
        </div>
        
        <script>
            document.addEventListener('DOMContentLoaded', () => {
                const nextBtns = document.querySelectorAll('.next-step');
                const prevBtns = document.querySelectorAll('.prev-step');
                const formSteps = document.querySelectorAll('.form-step');
                const stepIndicators = document.querySelectorAll('.step-indicator');
                let currentStep = 0;

                // Validation regex
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                const phoneRegex = /^[\d\s\-\+\(\)]{10,20}$/;

                // File storage variables
                let resumeFileBase64 = null;
                let resumeFileName = '';
                let coverFileBase64 = null;
                let coverFileName = '';
                let cnicFileBase64 = null;
                let cnicFileName = '';

                function setupFileUpload(inputId, boxId, nameDisplayId, callback) {
                    const fileInput = document.getElementById(inputId);
                    const box = document.getElementById(boxId);
                    const nameDisplay = document.getElementById(nameDisplayId);

                    // Drag and drop events
                    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                        box.addEventListener(eventName, preventDefaults, false);
                    });
                    function preventDefaults(e) { e.preventDefault(); e.stopPropagation(); }

                    ['dragenter', 'dragover'].forEach(eventName => {
                        box.addEventListener(eventName, () => box.style.borderColor = 'var(--primary)', false);
                    });
                    ['dragleave', 'drop'].forEach(eventName => {
                        box.addEventListener(eventName, () => box.style.borderColor = 'var(--border-color)', false);
                    });

                    box.addEventListener('drop', (e) => {
                        const dt = e.dataTransfer;
                        const files = dt.files;
                        if(files.length > 0) handleFile(files[0]);
                    });

                    fileInput.addEventListener('change', function(e) {
                        if(this.files.length > 0) handleFile(this.files[0]);
                    });

                    function handleFile(file) {
                        // Check size limit (e.g., max 4MB to avoid Vercel limit)
                        if(file.size > 4 * 1024 * 1024) {
                            alert('File is too large. Please upload a file smaller than 4MB.');
                            return;
                        }
                        nameDisplay.style.display = 'block';
                        nameDisplay.textContent = 'Selected: ' + file.name;
                        
                        const reader = new FileReader();
                        reader.onload = function(e) {
                            const base64String = e.target.result.split(',')[1];
                            callback(base64String, file.name);
                        };
                        reader.readAsDataURL(file);
                    }
                }

                // Setup file inputs
                setupFileUpload('file_resume', 'resume-box', 'name_resume', (b64, name) => { resumeFileBase64 = b64; resumeFileName = name; });
                setupFileUpload('file_cover', 'cover-box', 'name_cover', (b64, name) => { coverFileBase64 = b64; coverFileName = name; });
                setupFileUpload('file_cnic', 'cnic-box', 'name_cnic', (b64, name) => { cnicFileBase64 = b64; cnicFileName = name; });

                function updateFormSteps() {
                    formSteps.forEach((step, index) => {
                        step.style.display = index === currentStep ? 'block' : 'none';
                    });
                    
                    stepIndicators.forEach((indicator, index) => {
                        const circle = indicator.querySelector('.step-circle');
                        const label = indicator.querySelector('.step-label');
                        if (index === currentStep) {
                            circle.style.borderColor = 'var(--primary)';
                            circle.style.color = 'var(--primary)';
                            circle.style.backgroundColor = 'var(--bg-secondary)';
                            label.style.color = 'var(--primary)';
                        } else if (index < currentStep) {
                            circle.style.borderColor = 'var(--primary)';
                            circle.style.color = 'white';
                            circle.style.backgroundColor = 'var(--primary)';
                            label.style.color = 'var(--text-color)';
                        } else {
                            circle.style.borderColor = 'var(--text-muted)';
                            circle.style.color = 'var(--text-muted)';
                            circle.style.backgroundColor = 'var(--bg-secondary)';
                            label.style.color = 'var(--text-muted)';
                        }
                    });
                }

                nextBtns.forEach(btn => {
                    btn.addEventListener('click', () => {
                        const currentStepEl = formSteps[currentStep];
                        const requiredInputs = currentStepEl.querySelectorAll('input[required]');
                        let isValid = true;
                        
                        requiredInputs.forEach(input => {
                            let inputValid = true;
                            if(!input.value.trim()) {
                                inputValid = false;
                            } else if (input.type === 'email' && !emailRegex.test(input.value)) {
                                inputValid = false;
                                document.getElementById('email_error').style.display = 'block';
                            } else if (input.type === 'tel' && !phoneRegex.test(input.value)) {
                                inputValid = false;
                                document.getElementById('phone_error').style.display = 'block';
                            }
                            
                            if (!inputValid && input.type !== 'radio') {
                                isValid = false;
                                input.style.borderColor = 'red';
                            } else if (input.type !== 'radio') {
                                input.style.borderColor = 'var(--border-color)';
                            }
                        });

                        // Clear errors on correct input
                        const emailInput = document.getElementById('app_email');
                        if(emailInput && emailRegex.test(emailInput.value)) document.getElementById('email_error').style.display = 'none';
                        const phoneInput = document.getElementById('app_phone');
                        if(phoneInput && phoneRegex.test(phoneInput.value)) document.getElementById('phone_error').style.display = 'none';
                        
                        if (isValid && currentStep < formSteps.length - 1) {
                            currentStep++;
                            updateFormSteps();
                        }
                    });
                });

                prevBtns.forEach(btn => {
                    btn.addEventListener('click', () => {
                        if (currentStep > 0) {
                            currentStep--;
                            updateFormSteps();
                        }
                    });
                });
                
                // Add focus styles dynamically
                const allInputs = document.querySelectorAll('#career-application-form input[type="text"], #career-application-form input[type="email"], #career-application-form input[type="tel"], #career-application-form input[type="number"], #career-application-form textarea');
                allInputs.forEach(input => {
                    input.addEventListener('focus', () => {
                        input.style.borderColor = 'var(--primary)';
                        input.style.boxShadow = '0 0 0 3px rgba(139, 92, 246, 0.1)';
                    });
                    input.addEventListener('blur', () => {
                        if (input.hasAttribute('required') && !input.value.trim()) {
                            input.style.borderColor = 'red';
                        } else {
                            input.style.borderColor = 'var(--border-color)';
                        }
                        input.style.boxShadow = 'none';
                    });
                });

                document.getElementById('career-application-form').addEventListener('submit', async function(e) {
                    e.preventDefault();
                    
                    // Final Validation for Step 4
                    const resumeLink = document.getElementById('link_resume').value.trim();
                    const cnicFile = cnicFileBase64;
                    let isValid = true;
                    
                    if (!resumeFileBase64 && !resumeLink) {
                        alert('Please upload your Resume or provide a link.');
                        isValid = false;
                    }
                    if (!cnicFile) {
                        alert('Please upload your CNIC or B-Form.');
                        isValid = false;
                    }

                    if (!isValid) return;

                    const submitBtn = document.getElementById('submit_btn');
                    const submitMsg = document.getElementById('submit_msg');
                    submitBtn.style.display = 'none';
                    submitMsg.style.display = 'inline-block';
                    submitMsg.textContent = 'Processing your application... Please wait.';

                    const payload = {
                        type: document.querySelector('input[name="application_type"]:checked').value,
                        name: document.getElementById('app_name').value.trim(),
                        email: document.getElementById('app_email').value.trim(),
                        phone: document.getElementById('app_phone').value.trim(),
                        address: document.getElementById('app_address').value.trim(),
                        job_title: document.getElementById('app_job_title').value.trim(),
                        experience: document.getElementById('app_experience').value.trim(),
                        salary: document.getElementById('app_salary').value.trim(),
                        education: document.getElementById('app_education').value.trim(),
                        certifications: document.getElementById('app_certifications').value.trim(),
                        resume_link: resumeLink,
                        cover_link: document.getElementById('link_cover').value.trim(),
                        files: []
                    };

                    if (resumeFileBase64) {
                        payload.files.push({ name: resumeFileName, content: resumeFileBase64 });
                    }
                    if (coverFileBase64) {
                        payload.files.push({ name: coverFileName, content: coverFileBase64 });
                    }
                    if (cnicFileBase64) {
                        payload.files.push({ name: cnicFileName, content: cnicFileBase64 });
                    }

                    try {
                        const response = await fetch('/api/career', {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify(payload)
                        });

                        const result = await response.json();
                        
                        if (response.ok) {
                            submitMsg.style.color = 'green';
                            submitMsg.textContent = 'Application submitted successfully! We will be in touch.';
                            setTimeout(() => {
                                this.reset();
                                currentStep = 0;
                                resumeFileBase64 = null; coverFileBase64 = null; cnicFileBase64 = null;
                                document.querySelectorAll('.file-name-display').forEach(el => el.style.display = 'none');
                                updateFormSteps();
                                submitBtn.style.display = 'inline-block';
                                submitMsg.style.display = 'none';
                                submitMsg.style.color = 'var(--primary)';
                            }, 3000);
                        } else {
                            throw new Error(result.error || 'Failed to submit application');
                        }
                    } catch (error) {
                        console.error('Error submitting application:', error);
                        submitMsg.style.color = 'red';
                        submitMsg.textContent = 'Error: ' + error.message;
                        setTimeout(() => {
                            submitBtn.style.display = 'inline-block';
                            submitMsg.style.display = 'none';
                            submitMsg.style.color = 'var(--primary)';
                        }, 5000);
                    }
                });
            });
        </script>
    </section>"""

# Replace the block
pattern = re.compile(r'<section id="application-form".*?<!-- Careers Page Specific FAQs -->', re.DOTALL)
new_content = pattern.sub(new_form + '\n\n    <!-- Careers Page Specific FAQs -->', content)

with open('careers.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
