$trustBlock = Get-Content trust_block.html -Raw

function Fix-TrustBlock {
    param ([string]$FilePath, [string]$InsertMarker)
    
    $content = Get-Content $FilePath -Raw
    
    # Remove all existing trust building blocks
    $pattern = "(?s) *<!-- Global Trust-Building Sections -->.*?<!-- End Global Trust-Building Sections -->[\r\n]*"
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, $pattern, "")
    
    # Insert the block once before the marker
    $insertIndex = $content.IndexOf($InsertMarker)
    if ($insertIndex -ge 0) {
        $content = $content.Insert($insertIndex, $trustBlock + "`n")
        Set-Content -Path $FilePath -Value $content -NoNewline
        Write-Host "Fixed $FilePath"
    } else {
        Write-Host "Marker not found in $FilePath"
    }
}

$mainPages = @(
    @("index.html", "    <!-- Global CTA -->"),
    @("about.html", "    <!-- Global CTA -->"),
    @("services.html", "    <!-- Global CTA -->"),
    @("contact.html", "    <!-- Contact Page Specific FAQs -->")
)

foreach ($page in $mainPages) {
    Fix-TrustBlock -FilePath $page[0] -InsertMarker $page[1]
}

$services = @('wordpress-development.html', 'shopify-stores.html', 'advanced-seo.html', 'video-editing.html', 'content-writing.html', 'social-media-management.html')
foreach ($svc in $services) {
    Fix-TrustBlock -FilePath $svc -InsertMarker "    <!-- Final CTA & Form Section -->"
}
