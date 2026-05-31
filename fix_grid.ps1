$services = @('wordpress-development.html', 'shopify-stores.html', 'advanced-seo.html', 'video-editing.html', 'content-writing.html', 'social-media-management.html')

foreach ($svc in $services) {
    $content = Get-Content $svc -Raw
    
    # Regex to find the whole Features Section
    $sectionRegex = '(?s)    <!-- Features Section -->.*?<section class="impactful-services".*?<h2>(.*?)</h2>.*?<div class="service-card (.*?)".*?<i class="fa-solid (.*?)".*?<ul class="features-list">(.*?)</ul>.*?</section>'
    
    if ($content -match $sectionRegex) {
        $title = $matches[1]
        $theme = $matches[2]
        $icon = $matches[3]
        $listHtml = $matches[4]
        
        # Extract the features
        $featureRegex = '<li><i class="fa-solid fa-check check"></i>\s*(.*?)</li>'
        $features = [regex]::Matches($listHtml, $featureRegex) | ForEach-Object { $_.Groups[1].Value }
        
        # Build new HTML
        $newHtml = "    <!-- Features Section -->`n"
        $newHtml += "    <section class=`"impactful-services`" style=`"padding: 5rem 0;`">`n"
        $newHtml += "        <div class=`"container services-container`">`n"
        $newHtml += "            <div class=`"services-header`" style=`"text-align: center; margin-bottom: 40px;`">`n"
        $newHtml += "                <h2>$title</h2>`n"
        $newHtml += "            </div>`n"
        $newHtml += "            <div class=`"main-content-wrapper`">`n"
        $newHtml += "                <div>`n"
        
        foreach ($f in $features) {
            $newHtml += "                    <div class=`"service-card $theme`" style=`"padding: 2rem; border-radius: 1rem; text-align: center; box-shadow: var(--shadow); background-color: white;`">`n"
            $newHtml += "                        <i class=`"fa-solid $icon`" style=`"font-size: 2rem; color: var(--primary); margin-bottom: 1rem;`"></i>`n"
            $newHtml += "                        <h4 style=`"margin: 0; font-size: 1.1rem;`">$f</h4>`n"
            $newHtml += "                    </div>`n"
        }
        
        $newHtml += "                </div>`n"
        $newHtml += "            </div>`n"
        $newHtml += "        </div>`n"
        $newHtml += "    </section>"
        
        # Replace in file
        $content = $content -replace $sectionRegex, $newHtml
        Set-Content -Path $svc -Value $content -NoNewline
        Write-Host "Updated $svc"
    } else {
        Write-Host "Could not find Features Section in $svc"
    }
}
