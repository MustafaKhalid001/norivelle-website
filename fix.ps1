
$files = Get-ChildItem -Filter "*.html" | Where-Object { $_.Name -in "advanced-seo.html", "content-writing.html", "shopify-stores.html", "social-media-management.html", "video-editing.html", "wordpress-development.html" }
foreach ($file in $files) {
    $content = [IO.File]::ReadAllText($file.FullName)
    # The corrupted block starts right after the first `      <!-- End Global Trust-Building Sections -->`
    # and ends at `    <!-- FAQ Section -->`.
    # Wait, there are TWO `<!-- End Global Trust-Building Sections -->` now!
    # Because my script duplicated the entire section.
    
    # We want to delete everything from the FIRST `<!-- End Global Trust-Building Sections -->` 
    # to the SECOND `<!-- End Global Trust-Building Sections -->` inclusive.
    # Actually, the string to match is `      <!-- End Global Trust-Building Sections -->\r\n\r\n                    <div class="service-card theme-` all the way to `      <!-- End Global Trust-Building Sections -->`
    
    $pattern = "(?s)      <!-- End Global Trust-Building Sections -->.*?      <!-- End Global Trust-Building Sections -->"
    $replacement = "      <!-- End Global Trust-Building Sections -->"
    $content = $content -replace $pattern, $replacement
    
    # Next, we need to fix the missing footer tags that were deleted:
    # `    \r\n            <div class="footer-grid">`
    # SHOULD BE:
    # `    \r\n<footer>\r\n        <div class="container">\r\n            <div class="footer-grid">`
    $pattern2 = "(?s)    \r?\n            <div class=`"footer-grid`">"
    $replacement2 = "    `n<footer>`n        <div class=`"container`">`n            <div class=`"footer-grid`">"
    $content = $content -replace $pattern2, $replacement2
    
    [IO.File]::WriteAllText($file.FullName, $content)
}
Write-Host "Fixed!"

