#push to github

echo Enter a comment for this git push:
read varname
echo Comment: $varname

git add .
git commit -m $varname
git push