# Start Project using Github 01

> This is for helping cooperation a team project efficiently using the Github system, especially this is about the setting of the whole team's computer environment when you just about to start your team project.



#### Contributor vs Collaborator?

- The `contributor` means who is not the master of the project, but all the participants who are committing to the same project.
- If you are a `contributor`, then you don't have the right to access for push, so you could fork the project to your repository (like copying), and only a `project manager` and `collaborator` can push.
- You could do lots of things in the repository you forked, then also can `push` all the changes that you made to original repository using `pull request`.
- You could do lots of things in the repository you forked, they also can `push` all the changes that you made to an original repository using a `pull request`.
- `collaborator` is a co-project manager, so who has all the rights to `push` and `pull` as well. The only difference between contributor and collaborator is everyone can be a `contributor` by doing `pull request`, but `collaborator` needs to get access from a project master.



## Github Project with Collaborator

> With the above explanation, you could put collaborators in your repository(project) 

#### (1) The project manager needs to create a new repository

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_00.JPG?raw=true" style="zoom:80%;" />

#### (2) The project manager should add collaborators in the Settings tab

<img src="https://t1.daumcdn.net/cfile/tistory/9944DB4B5BD988A40A" alt="https://hyoje420.tistory.com/41" style="zoom:80%;" />

#### (3) Put collaborator's Github ID in the searching place

- You can just add or search the collaborator's ID and click the `[Add collaborator]`.

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_04.JPG?raw=true" alt="04" style="zoom:80%;" />

#### (4) The invitation email will be sent automatically

- After the step3, the invitation is just going to their connected email with Github ID.

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_02.jpg?raw=true" style="zoom:80%;" />

#### (5) The collaborators can find the invitation in their own email or check the link from the project manager

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_05.JPG?raw=true" alt="05" style="zoom: 80%;" />

#### (6) Go to the repository of your project, then clone it with master branch

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_01.JPG?raw=true" alt="01" style="zoom:80%;" />

#### (7) `git bash` clone the master branch to your local computer

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_06.JPG?raw=true" alt="06" style="zoom:80%;" />

#### (8) You could check the cloning and master branch in your local

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_07.JPG?raw=true" alt="07" style="zoom:80%;" />

#### (9) Using below command line to create a new branch of yours [brchB]

```shell
$ git checkout -b [branch name]

# above command line means add below 2 commands line together
$ git branch [branch name]
$ git checkout [branch name]
```

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_08.jpg?raw=true" alt="08" style="zoom:80%;" />

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_09.jpg?raw=true" alt="09" style="zoom:80%;" />

> After using the command line to create your own branch, then you could check the changes of your branch to `brchB`. Also, `git checkout` would let you change the master branch and your branch easily.

#### (10) To check the branches that collaborators created in the repository page

<img src="https://github.com/dannylee93/Images/blob/master/Image%20Analysis%20A.I/Github_Project_10.jpg?raw=true" alt="10" style="zoom:80%;" />

#### (11) After work is done, use command line below to commit

```shell
git push origin [your own branch name]
```



## References

- Webpages

- https://hyoje420.tistory.com/41
- https://victorydntmd.tistory.com/91



