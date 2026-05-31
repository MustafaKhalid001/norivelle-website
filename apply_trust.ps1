$trustBlock = Get-Content trust_block.html -Raw

function Apply-TrustBlock {
    param (
        [string]$FilePath,
        [string]$InsertMarker
    )
    
    $content = Get-Content $FilePath -Raw
    
    $startStr = "    <!-- Global Trust-Building Sections -->"
    $endStr = "    <!-- End Global Trust-Building Sections -->`n"
    
    $startIndex = $content.IndexOf($startStr)
    if ($startIndex -ge 0) {
        $endIndex = $content.IndexOf($endStr) + $endStr.Length
        $content = $content.Remove($startIndex, $endIndex - $startIndex)
    }
    
    $insertIndex = $content.IndexOf($InsertMarker)
    if ($insertIndex -ge 0) {
        $content = $content.Insert($insertIndex, $trustBlock + "`n")
        Set-Content -Path $FilePath -Value $content -NoNewline
        Write-Host "Updated $FilePath"
    } else {
        Write-Host "Marker not found in $FilePath"
    }
}

Apply-TrustBlock -FilePath "index.html" -InsertMarker "    <!-- Global CTA -->"
Apply-TrustBlock -FilePath "about.html" -InsertMarker "    <!-- Global CTA -->"
Apply-TrustBlock -FilePath "services.html" -InsertMarker "    <!-- Global CTA -->"
Apply-TrustBlock -FilePath "contact.html" -InsertMarker "    <!-- Contact Page Specific FAQs -->"

$services = @('wordpress-development.html', 'shopify-stores.html', 'advanced-seo.html', 'video-editing.html', 'content-writing.html', 'social-media-management.html')
foreach ($svc in $services) { Apply-TrustBlock -FilePath $svc -InsertMarker '    <!-- Final CTA & Form Section -->' }
