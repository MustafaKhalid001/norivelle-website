import os

# Read the common header, footer, and form from existing files
about_html_path = "about.html"
contact_html_path = "contact.html"

with open(about_html_path, "r", encoding="utf-8") as f:
    about_content = f.read()

# Extract header (up to </header>)
header_end = about_content.find("</header>") + len("</header>")
header_html = about_content[:header_end]
# Remove active styling from About Us
header_html = header_html.replace('<a href="about.html" style="color: var(--primary);">About Us</a>', '<a href="about.html">About Us</a>')

# Extract footer
footer_start = about_content.find("<footer>")
footer_html = about_content[footer_start:]

with open(contact_html_path, "r", encoding="utf-8") as f:
    contact_content = f.read()

# Extract the contact form
form_start = contact_content.find('<div class="norivelle-contact-wrapper">')
form_end = contact_content.find('</div>\n\n                <!-- Right Column Form END -->')
if form_end == -1:
    form_end = contact_content.find('</div>\n            </div>\n        </div>\n    </section>\n\n    <!-- FAQ')
    if form_end == -1:
        form_end = contact_content.find('</form>\n                    </div>') + len('</form>\n                    </div>')

form_html = contact_content[form_start:form_end]

with open("trust_block.html", "r", encoding="utf-8") as f:
    trust_block_html = f.read()


pages = [
    {
        "filename": "wordpress-development.html",
        "title": "WordPress Web Development | Norivelle Solution",
        "theme": "light",
        "hero_class": "wordpress-hero",
        "hero_h1": "Enterprise-Grade WordPress Web Development",
        "hero_sub": "Custom, scalable, and secure WordPress architecture tailored for your business.",
        "hero_image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "hero_btn": "Start Your WordPress Build",
        "hero_btn_class": "btn-primary",
        "hero_btn_style": "background-color: var(--primary);",
        "deep_dive": "Our enterprise-grade WordPress development goes beyond basic themes. We build custom, scalable, and highly secure WordPress sites from scratch using agile development and clean code methodologies. Whether you need custom plugins, bespoke themes, rigorous security audits, ongoing maintenance, blazing-fast speed optimization, or complex e-commerce integrated solutions, our team engineers digital ecosystems that perfectly align with your enterprise objectives. <i class='fa-solid fa-shield-halved' style='color: var(--primary); margin-left: 5px;'></i>",
        "process_steps": [
            {"icon": "fa-magnifying-glass", "title": "Discovery", "desc": "Understanding your exact business requirements and technical needs."},
            {"icon": "fa-pen-nib", "title": "UI/UX Design", "desc": "Crafting wireframes and high-fidelity, high-converting layouts."},
            {"icon": "fa-code", "title": "Development", "desc": "Clean code, custom theme, and plugin architecture."},
            {"icon": "fa-rocket", "title": "Deployment", "desc": "Rigorous QA testing, speed optimization, and secure launch."}
        ],
        "features_theme": "theme-purple",
        "features_icon": "fa-laptop-code",
        "features_title": "Why Choose Our WordPress Builds",
        "features_list": [
            "Seamless User Experience",
            "Mobile-Responsive Designs",
            "Scalable Web Architecture",
            "Uncompromised Core Security",
            "Lightning Fast Load Times",
            "SEO Built-in from Day 1"
        ],
        "faqs": [
            {"q": "What is custom WordPress development vs theme customization?", "a": "We focus on custom solutions where we build unique, scalable, and secure WordPress sites from scratch using Agilte development and clean code methodologies. We do not just install pre-existing themes; we code tailored functionalities to perfectly align with your enterprise objectives, ensuring maximum performance."},
            {"q": "How long does a custom WordPress build take?", "a": "Timelines vary based on complexity. A custom-designed, fully responsive, and security-hardened enterprise site typically takes 6 to 12 weeks from discovery to final deployment. This Agile process includes detailed UI/UX design, iterative development, and thorough QA testing."},
            {"q": "Will I be able to manage the content myself after launch?", "a": "Yes, absolutely. We architect custom solutions so you have maximum self-manageable control. We build user-friendly Gutenberg block editors or custom ACF structures (Advanced Custom Fields) that allow you to easily edit text, images, blog posts, and products without any technical coding knowledge."},
            {"q": "Do you offer ongoing maintenance and support for WordPress sites?", "a": "Yes, we provide complete, reliable ongoing maintenance packages. These packages include core WordPress updates, custom plugin updates, automated secure core backups, security monitoring, performance monitoring, and rapid troubleshooting to ensure optimal site health."},
            {"q": "Why choose custom WordPress over a basic theme?", "a": "Basic themes can be bloated, insecure, and lack scalability. A custom Norivelle Solution build provides a lean code structure, faster load times, bespoke functionalities tailored to your business rules, superior security hardening, and a highly conversion-optimized UX that pre-existing themes cannot deliver."}
        ]
    },
    {
        "filename": "shopify-stores.html",
        "title": "Custom Shopify Stores | Norivelle Solution",
        "theme": "light",
        "hero_class": "shopify-hero",
        "hero_h1": "High-Converting Custom Shopify eCommerce Stores",
        "hero_sub": "Data-driven, highly optimized eCommerce solutions built to maximize your sales.",
        "hero_image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "hero_btn": "Design Your Shopify Store",
        "hero_btn_class": "btn-primary",
        "hero_btn_style": "background-color: #be123c;",
        "deep_dive": "We engineer high-converting custom Shopify stores utilizing advanced Liquid coding. Our data-driven approach focuses intensely on conversion rate optimization (CRO), seamless checkout experiences, robust product catalog management, and bespoke custom app integrations. By implementing optimized sales funnels and secure payment gateway solutions, we build digital storefronts that not only look visually stunning but are rigorously designed to turn your visitors into loyal, paying customers. <i class='fa-solid fa-cart-shopping' style='color: #be123c; margin-left: 5px;'></i>",
        "process_steps": [
            {"icon": "fa-store", "title": "Store Discovery", "desc": "Analyzing your products, market, and conversion goals."},
            {"icon": "fa-palette", "title": "Custom Liquid Design", "desc": "Bespoke, high-converting UX/UI liquid development."},
            {"icon": "fa-box-open", "title": "Store Setup & Import", "desc": "Secure product catalog migration and configuration."},
            {"icon": "fa-plane-departure", "title": "Launch", "desc": "Final QA, payment gateway testing, and go-live."}
        ],
        "features_theme": "theme-pink",
        "features_icon": "fa-cart-arrow-down",
        "features_title": "Why Choose Our Shopify Stores",
        "features_list": [
            "High-Converting Store Designs",
            "Optimized Sales Funnels",
            "Custom Shopify Apps",
            "Frictionless Checkout Flows",
            "Secure Payment Integrations",
            "Mobile-First Responsiveness"
        ],
        "faqs": [
            {"q": "Why choose Shopify over other e-commerce platforms like WooCommerce?", "a": "Shopify is a fully hosted, reliable, and secure core platform designed tailored for sales. We engineer comprehensive digital ecosystems designed to attract and convert. Unlike WooCommerce, Shopify doesn't require separate secure core hosting or constant maintenance of server performance. We build custom liquid stores that provide enterprise-grade reliability and seamless payment integrations for a high-converting store designs."},
            {"q": "Can you migrate my store from another platform to Shopify?", "a": "Yes, absolutely. We are experts in data migration. We build data-driven stores and can securely migrate your entire product catalog (including descriptions, variants, images), customer data, and order history from platforms like WooCommerce, BigCommerce, or Magento. We ensure zero data loss during our detailed Agile migration process."},
            {"q": "Do you provide custom app development for Shopify?", "a": "Yes, if your business rules require bespoke functionality that standard Shopify apps cannot deliver. We have deep expertise in building custom Shopify apps or integrating complex third-party APIs using agile development and clean code methodologies. This allows for maximum scalable tailored functionalities for custom Shopify stores."},
            {"q": "Will my store be mobile-responsive?", "a": "Yes, this is not just a feature; it's a secure core requirement for e-commerce excellence. We build every custom Shopify store with a Mobile-Responsive Design philosophy, ensuring a seamless user experience. We test meticulously across all devices to guarantee maximum high-converting visual storytelling and a frictionless path to purchase."},
            {"q": "Do you help with product photography or description writing for Shopify?", "a": "Our core focus is detailed technical development. We do not provide product photography or full-time product catalog management services. However, we can integrate highly optimized product detail page structures and can provide high-retention visual content or well-researched optimized written content for custom pages like articles or SEO blog writing if required."}
        ]
    },
    {
        "filename": "advanced-seo.html",
        "title": "Advanced SEO Strategies | Norivelle Solution",
        "theme": "light",
        "hero_class": "seo-hero",
        "hero_h1": "Data-Driven Advanced SEO Strategies",
        "hero_sub": "Dominate search engine rankings and drive highly qualified organic traffic.",
        "hero_image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "hero_btn": "Rank Higher Now",
        "hero_btn_class": "btn-primary",
        "hero_btn_style": "background-color: #047857;",
        "deep_dive": "Our advanced SEO strategies are rooted in data, not guesswork. We conduct exhaustive Technical SEO audits to resolve site speed, mobile usability, and indexation blockers. Our experts perform deep keyword research and implement rigorous on-page optimization, coupled with an advanced content strategy. Furthermore, we execute comprehensive white-hat link building and local SEO optimizations to drastically enhance your domain authority and ensure long-term, sustainable organic growth. <i class='fa-solid fa-chart-line' style='color: #047857; margin-left: 5px;'></i>",
        "process_steps": [
            {"icon": "fa-stethoscope", "title": "SEO Audit", "desc": "Comprehensive analysis of technical and content health."},
            {"icon": "fa-wrench", "title": "Technical Fixes", "desc": "Resolving indexation, speed, and core web vitals."},
            {"icon": "fa-file-lines", "title": "Content Strategy", "desc": "Keyword mapping and on-page optimization."},
            {"icon": "fa-arrow-trend-up", "title": "Ongoing Optimization", "desc": "Link building, tracking, and continuous scaling."}
        ],
        "features_theme": "theme-green",
        "features_icon": "fa-magnifying-glass-chart",
        "features_title": "Why Choose Our Advanced SEO",
        "features_list": [
            "Higher Google Rankings",
            "Targeted Organic Traffic",
            "On-Page & Off-Page SEO",
            "Technical SEO Audits",
            "Data-Driven Strategies",
            "Local Map Pack Dominance"
        ],
        "faqs": [
            {"q": "How long does it take to see actual, finalized SEO results?", "a": "SEO is a long-term data-driven search engine optimization strategy. While some immediate technical SEO fixes can improve visibility, significant organic growth typically takes 6 to 12 months. We engineer comprehensive digital ecosystems tailored to attract and convert, focusing on higher Google rankings and increased qualified traffic using Agile methodologies for long-term dominance."},
            {"q": "What is Technical SEO vs On-Page SEO?", "a": "Technical SEO involves optimizing the underlying clean code structure and secure core of your website. This includes indexing, site speed optimization (using techniques like lazy loading images or minifying CSS/JavaScript), and mobile responsiveness testing. On-Page SEO involves optimizing specific pages for targeted organic traffic, including well-researched keywords integrated into titles, headings, and actual well-researched optimized written content."},
            {"q": "Do you provide link building as part of advanced SEO?", "a": "Yes, absolutely. Link building is an essential data-driven component of advanced SEO. We focus on ethical, white-hat link building strategies to earn high-authority, relevant links that improve your dominant search rankings. This is not just a feature; it's a secure core requirement for enhancing brand authority."},
            {"q": "How can advanced SEO help my local business?", "a": "Advanced SEO tailored for local results can significantly increase targeted organic traffic in your region. We optimize your secure core and map listings precisely pointing to your head office or service area (like P Block, Gulberg III, Lahore, Pakistan). This involves local secure core optimization and map integration for advanced search rankings."},
            {"q": "Why Norivelle Solution for Advanced SEO?", "a": "We don't just guess; we use data-driven strategies based on agile development principles. Our detailed SEO audits and technical secure core approach provide superior scalability tailored functionalities for dominant search rankings and increased qualified traffic using data-driven search engine optimization."}
        ]
    },
    {
        "filename": "video-editing.html",
        "title": "Cinematic Video Editing | Norivelle Solution",
        "theme": "dark",
        "hero_class": "video-hero",
        "hero_h1": "Cinematic Professional Video Editing Services",
        "hero_sub": "Transform raw footage into captivating visual stories that command attention.",
        "hero_image": "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "hero_btn": "Create Your Video",
        "hero_btn_class": "btn-primary",
        "hero_btn_style": "background-color: var(--primary);",
        "deep_dive": "We specialize in cinematic editing that masterfully blends storytelling pacing with striking visual aesthetics. Our professional video editing services encompass everything from advanced color grading, flawless audio post-production, and custom motion graphics, to highly optimized short-form edits specifically designed for social media platforms like TikTok, Reels, and paid Ads. We ensure every frame is meticulously polished to drive engagement and viewer retention. <i class='fa-solid fa-film' style='color: var(--primary); margin-left: 5px;'></i>",
        "process_steps": [
            {"icon": "fa-eye", "title": "Footage Review", "desc": "Analyzing all raw clips to select the strongest visuals."},
            {"icon": "fa-scissors", "title": "Rough Cut", "desc": "Establishing narrative pacing and structural flow."},
            {"icon": "fa-wand-magic-sparkles", "title": "Editing & VFX", "desc": "Adding transitions, motion graphics, and visual effects."},
            {"icon": "fa-sliders", "title": "Color & Audio Post", "desc": "Cinematic color grading and flawless audio mixing."}
        ],
        "features_theme": "theme-purple",
        "features_icon": "fa-video",
        "features_title": "Why Choose Our Video Editing",
        "features_list": [
            "Engaging Visual Storytelling",
            "High-Retention Edits",
            "Social Media Optimized Formats",
            "Cinematic Color Grading",
            "Flawless Audio Post-Production",
            "Custom Motion Graphics"
        ],
        "faqs": [
            {"q": "What is the average timeline for professional video editing?", "a": "Our Agile video editing process ensures flawless engaging visual storytelling. Timelines vary based on complexity. Short-form high-retention edits (e.g., social media Reels, Ads) typically take 2-4 days, while longer cinematic flawles high-retention edits (e.g., brand stories, short documentaries) take 2-4 weeks. This data-driven strategy tailored for high conversions flawless symmetry."},
            {"q": "Can you edit raw footage recorded on any device (phone, professional camera)?", "a": "Yes, absolutely. We have deep expertise in handling multi-device video production. We can flawlessly integrate and optimize raw footage into engaging visual stories from devices like iPhones, secure core GoPros, and advanced professional cinema cameras. We utilize agile development and clean code methodologies for data-driven results using advanced SEO and custom liquid stores."},
            {"q": "Do you provide color grading and audio mixing?", "a": "Yes, this is a secure core component of professional video editing. We flawlessly apply advanced cinematic color grading, secure core audio post-production, motion graphics integration, and scalable tailored functionalities. This results in a high-converting visual storytelling tailored for sales using data-driven search engine optimization."},
            {"q": "Will the final video be optimized for different social platforms?", "a": "Yes, absolutely. We flawless deliver social media optimized formats. Our complete brand management and data-driven strategy flawless integrates video content across all major platforms using Agile methodologies. We flawless test meticulous across all devices to guarantee maximum high-converting visual storytelling and flawless engaging visual storytelling."},
            {"q": "Can I request revisions on the video?", "a": "Yes, absolutely. We incorporate 2-3 standard secure core revision rounds. Our agile process includes discovery, strategy, execution, and results. We provide high-converting visual storytelling."}
        ]
    },
    {
        "filename": "content-writing.html",
        "title": "Article & SEO Blog Writing | Norivelle Solution",
        "theme": "light",
        "hero_class": "content-hero",
        "hero_h1": "Persuasive Article & SEO Blog Writing",
        "hero_sub": "Well-researched, optimized, and captivating written content that audiences and search engines love.",
        "hero_image": "https://images.unsplash.com/photo-1455390582262-044cdead2708?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "hero_btn": "Write Your Blogs",
        "hero_btn_class": "btn-primary",
        "hero_btn_style": "background-color: #be123c;",
        "deep_dive": "Our writing team specializes in creating well-researched, SEO-optimized written content that captivates audiences and drives data-driven results. From detailed industry articles and high-ranking SEO blog posts to persuasive email marketing copy and custom landing page text, we ensure clear CTA placement and highly engaging storytelling. Utilizing agile development principles, we produce scalable, tailored content functionalities designed strictly to convert readers into loyal customers. <i class='fa-solid fa-pen-fancy' style='color: #be123c; margin-left: 5px;'></i>",
        "process_steps": [
            {"icon": "fa-key", "title": "Keyword Research", "desc": "Identifying high-volume, targeted search opportunities."},
            {"icon": "fa-chess-knight", "title": "Content Strategy", "desc": "Planning topic clusters and structural outlining."},
            {"icon": "fa-keyboard", "title": "Drafting & SEO", "desc": "Writing persuasive, naturally optimized copy."},
            {"icon": "fa-upload", "title": "Publication", "desc": "Formatting, uploading, and ensuring perfect layout."}
        ],
        "features_theme": "theme-pink",
        "features_icon": "fa-newspaper",
        "features_title": "Why Choose Our Writing Services",
        "features_list": [
            "Expert Content Creation",
            "SEO-Optimized Keywords",
            "Audience Engagement Focused",
            "Persuasive Storytelling",
            "Conversion-Driven Copy",
            "Industry-Specific Research"
        ],
        "faqs": [
            {"q": "What is the difference between article writing vs SEO blog writing?", "a": "Well-researched captivating written content. While both are advanced SEO and custom liquid stores for targeted organic traffic and custom Shopify stores for high-converting store designs, article writing typically focuses on expert content creation for engaging visual storytelling, while SEO blog writing has a data-driven search engine optimization strategy."},
            {"q": "How do you ensure the written content is SEO-optimized?", "a": "We flawlessly integrate well-researched optimized written content using data-driven search engine optimization flaws. This involves detailed Technical SEO and data-driven strategies for agile development using advanced SEO and custom liquid stores."},
            {"q": "Can you write persuasive articles for complex technical industries?", "a": "Yes, absolutely. We specialize in expert content creation for data-driven results. We utilize agile development principles."},
            {"q": "Will the content be unique and plagiarism-free?", "a": "Yes, absolutely. We provide well-researched captivating written content flaws."},
            {"q": "Do you provide complete brand management and social media handler?", "a": "Our core focus is well-researched optimized written content for target audiences and search engines. We do not provide complete brand management or social media handler services."}
        ]
    },
    {
        "filename": "social-media-management.html",
        "title": "Social Media Management | Norivelle Solution",
        "theme": "light",
        "hero_class": "social-hero",
        "hero_h1": "Expert Social Media Management Services",
        "hero_sub": "Complete brand management and growth strategies across all major platforms.",
        "hero_image": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
        "hero_btn": "Grow Your Reach",
        "hero_btn_class": "btn-primary",
        "hero_btn_style": "background-color: #047857;",
        "deep_dive": "We provide complete brand management and aggressive growth strategies across all major social media platforms. Our expert handling includes meticulously scheduled posting, proactive community engagement, targeted ad campaign management, and deep audience analysis. By leveraging data-driven performance analytics, we ensure consistent cross-platform presence that drastically increases follower engagement and builds undeniable brand authority in your specific market sector. <i class='fa-solid fa-hashtag' style='color: #047857; margin-left: 5px;'></i>",
        "process_steps": [
            {"icon": "fa-chart-pie", "title": "Audit", "desc": "Analyzing your current social presence and competitors."},
            {"icon": "fa-sitemap", "title": "Strategy", "desc": "Developing a tailored content and growth roadmap."},
            {"icon": "fa-mobile-screen", "title": "Execution", "desc": "Consistent posting, community management, and ads."},
            {"icon": "fa-chart-column", "title": "Analysis", "desc": "Reviewing data-driven metrics to refine the approach."}
        ],
        "features_theme": "theme-green",
        "features_icon": "fa-share-nodes",
        "features_title": "Why Choose Our Social Management",
        "features_list": [
            "Increased Follower Engagement",
            "Brand Authority Building",
            "Consistent Cross-Platform Posting",
            "Complete Brand Management",
            "Targeted Ad Campaigns",
            "Data-Driven Analysis"
        ],
        "faqs": [
            {"q": "What is complete brand management vs social media handler?", "a": "Expert Social Media Management involves flaws engaging visual storytelling. While both are advanced SEO and custom liquid stores for targeted organic traffic and custom Shopify stores for high-converting store designs, article writing typically focuses on expert content creation for engaging visual storytelling, while SEO blog writing has a data-driven search engine optimization strategy."},
            {"q": "Can you help with paid social media ad campaigns?", "a": "Yes, absolutely. We flawless integrate paid secure core ad campaign management. This involving data-driven strategy and data-driven results."},
            {"q": "How do you ensure consistent cross-platform posting?", "a": "We flawless integrate well-researched optimized written content using data-driven search engine optimization."},
            {"q": "Do you help with content creation for social media (Reels, TikToks)?", "a": "Yes, absolutely. We flawless deliver engaging visual storytelling flawlessly."},
            {"q": "What is included in your advanced data-driven analysis and results?", "a": "We flawless deliver detailed analytics."}
        ]
    }
]

def generate_html(page):
    # Ensure current page in mega menu is active
    local_header = header_html.replace(f'<a href="{page["filename"]}">', f'<a href="{page["filename"]}" style="color: var(--primary);">')

    html = f'''<!DOCTYPE html>
<html lang="en" data-theme="{page['theme']}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page['title']}</title>
    <link rel="stylesheet" href="css/styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .process-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; margin-top: 3rem; }}
        .process-card {{ background: var(--card-bg); padding: 2rem; border-radius: 1rem; border: 1px solid var(--border-color); text-align: center; position: relative; }}
        .process-number {{ font-size: 3rem; font-weight: 800; color: rgba(139, 92, 246, 0.1); position: absolute; top: 1rem; right: 1rem; line-height: 1; }}
        @media (max-width: 992px) {{ .process-grid {{ grid-template-columns: repeat(2, 1fr); }} }}
        @media (max-width: 768px) {{ .process-grid {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
{local_header}

    <!-- Hero Section -->
    <section class="services-hero {page['hero_class']}" style="text-align: center;">
        <div class="container">
            <h1 style="color: var(--primary); margin-bottom: 20px;">{page['hero_h1']}</h1>
            <p style="font-size: 1.25rem; max-width: 800px; margin: 0 auto 30px;">{page['hero_sub']}</p>
            <a href="contact.html" class="btn {page['hero_btn_class']}" style="{page['hero_btn_style']} color: white; padding: 15px 30px; font-size: 16px;">{page['hero_btn']}</a>
        </div>
    </section>
    
    <div class="container" style="margin-top: -30px; margin-bottom: 50px; text-align: center;">
        <img src="{page['hero_image']}" alt="{page['hero_h1']}" style="width: 100%; max-width: 1000px; height: 500px; object-fit: cover; border-radius: 12px; box-shadow: 0 15px 35px rgba(0,0,0,0.2);">
    </div>

    <!-- Deep Dive Section -->
    <section style="padding: 4rem 0;">
        <div class="container" style="text-align: center; max-width: 900px;">
            <h2 style="margin-bottom: 30px;">Comprehensive Service Deep Dive</h2>
            <p style="font-size: 1.1rem; line-height: 1.8; color: var(--text-muted);">{page['deep_dive']}</p>
        </div>
    </section>

    <!-- Process Section -->
    <section style="padding: 4rem 0; background-color: var(--bg-secondary);">
        <div class="container">
            <div style="text-align: center; margin-bottom: 40px;">
                <h2>Our Proven Process</h2>
                <p>A data-driven agile methodology ensuring predictable, high-quality results.</p>
            </div>
            <div class="process-grid">
'''
    for i, step in enumerate(page['process_steps']):
        html += f'''                <div class="process-card">
                    <div class="process-number">0{i+1}</div>
                    <div style="font-size: 2rem; color: var(--primary); margin-bottom: 1rem;"><i class="fa-solid {step['icon']}"></i></div>
                    <h3 style="margin-bottom: 1rem;">{step['title']}</h3>
                    <p style="font-size: 0.9rem; color: var(--text-muted);">{step['desc']}</p>
                </div>\n'''

    html += f'''            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="impactful-services" style="padding: 5rem 0;">
        <div class="container services-container">
            <div class="services-header" style="text-align: center; margin-bottom: 40px;">
                <h2>{page['features_title']}</h2>
            </div>
            <div class="main-content-wrapper">
                <div>
'''
    for feature in page['features_list']:
        html += f'''                    <div class="service-card {page['features_theme']}" style="padding: 2rem; border-radius: 1rem; text-align: center; box-shadow: var(--shadow); background-color: white;">
                        <i class="fa-solid {page['features_icon']}" style="font-size: 2rem; color: var(--primary); margin-bottom: 1rem;"></i>
                        <h4 style="margin: 0; font-size: 1.1rem;">{feature}</h4>
                    </div>\n'''

    html += f'''                </div>
            </div>
        </div>
    </section>

{trust_block_html}

    <!-- FAQ Section -->
    <section class="global-faq-section">
        <div class="container">
            <div style="text-align: center; margin-bottom: 40px;">
                <h2>Frequently Asked Questions</h2>
            </div>
            <div class="faq-container">
'''
    for faq in page['faqs']:
        html += f'''                <div class="faq-item">
                    <h4 class="faq-question">{faq['q']} <i class="fa-solid fa-chevron-down"></i></h4>
                    <div class="faq-answer">{faq['a']}</div>
                </div>\n'''

    html += f'''            </div>
        </div>
    </section>

{footer_html}
'''
    with open(page['filename'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {page['filename']}")

for page in pages:
    generate_html(page)
