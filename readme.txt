Install the pip (Python Package Installer) 
get-pip.py 
python get-pip.py 
pip install virtualenv
cd Stories\Innovation
Virtualen en 

url : https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/
python -m venv %systemdrive%%homepath%\my-venv
%systemdrive%%homepath%\my-venv\Scripts\activate.bat
url : https://www.techcoil.com/blog/how-to-create-a-python-3-virtual-environment-in-windows-10/
python -m venv %systemdrive%%homepath%\my-venv









    quiz = get_object_or_404(Cases, pk=pk)
    teacher = request.user.teacher
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.case = quiz
            question.teacher = teacher
            question.save()
            question.case.evaluer == True
            question.case.state = question.state
            messages.success(request, 'You may now add answers/options to the question.')
            
    else:
        return render(request, 'classroom/teachers/board/forms.html', {'quiz': quiz})

















Images : https://wsvincent.com/django-image-uploads/

 get texthttps://mlocati.github.io/articles/gettext-iconv-windows.html

			{% block content %}
									<div class="post">
										{% if post %}
											<div class="date">
												{{ post.published_date }}
											</div>
										{% endif %}
										<h2>{{ post.title_case}}</h2>
										{% if post.image_produit %}
										<picture><img src="{{ post.image_produit.url }}" alt="vous devez ajouter une figure"/></picture>
										 {% endif %}
										
										  </div>


git commit -m "initial commit"
git push origin master

Médical
Alimentaire
Agricole
Environnemental
Technologie
Aéronautique
Robotique
Astronomie
Mécatronique 
Electronique
Chimie
Biologie
Science
Biotechnologie
Mécanique
Géologie
Mathématiques
Physique 
Transport
Architecture
Télécommunications
Energie 
Medical
Agro-Food
Agriculture
Environmental
Technology
Aeronautics
Robotics
Astronomy
Mechatronics 
Electronics
Chemistry
Biology
Science
Biotechnology
Mechanics
Geology
Mathematics
Physical 
Transportation
Architecture
Telecommunications
Energy 