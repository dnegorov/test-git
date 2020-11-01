$num = $args[0]
$tag_ver = "v0.0." + $num.ToString()
echo $tag_ver

$f = (Get-Content .\README.md) 
$f[12] = '### Last version! ' + $tag_ver
$f | set-content .\README.md

$commit = "v" + $num.ToString()
$tag_descr = 'test tag ' + $num.ToString()

git add .
git commit -m $commit
git push
git tag -a $tag_ver -m $tag_descr
git push --tags
