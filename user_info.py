class UserInformation:
    def __init__(self):
        self.name = None
        self.age = None
        self.weight = None
        self.height = None
        self.gender = None
        self.goal = None
        self.days = None

    def basicInfoQuestions(self):
        self.name = input('Enter your name: ')
        self.age = int(input('Enter your age: '))
        self.weight = float(input('Enter your weight in pounds: '))
        self.height = float(input('Enter your height in cm: '))
        # gender_choices = {'F': 'female', 'M': 'male', 'N': 'non-binary'}
        # while self.gender not in gender_choices.keys():
        #     self.gender = input(f'Enter your gender [{"/".join(gender_choices.keys())}]: ').upper()
        # self.gender = gender_choices[self.gender]
        
        self.gender = {'F': 'female', 'M': 'male', 'N': 'non-binary', 'A': 'additional gender options','P': 'prefer not to say'}[input('Choose your gender:\n[F] female\n[M] male\n[N] non-binary\n[A] additional gender options\n[P] prefer not to say\n')]
        if self.gender == 'A':
            self.gender = input('Enter your gender: ')


        self.goal = {'1': 'Body Recomposition', '2': 'Lose Weight', '3': 'Gain Weight'}[input('Choose your body goal: [1] Body Recomposition, [2] Lose Weight, [3] Gain Weight ')]
        self.days = int(input('Enter the number of days a week you prefer to workout (between 1-6 days): '))


    def displayInfo(self):
        print('Welcome', self.name, '!')
        print('Age:', self.age)
        print('Weight:', self.weight, 'lbs')
        print('Height:', self.height, 'cm')
        print('Gender:', self.gender)
        print('Your fitness goal is', self.goal,'!')
        print('You want to workout', self.days, 'days per week')

# Create a new user and ask for their information
u1 = UserInformation()
u1.basicInfoQuestions()

# Display the user's information to make sure it works
u1.displayInfo()

# Exercises

# this is the detailed workout plan to chose from
exercise_presets = {
    'Lose Weight': ['Full Body Strength Training\nLateral Pulldowns(4x12)\nPull Ups(4x8)\nUpright Row(3x12)\nTricep Extension(3x12)\nCable Squat(4x12)','HIIT Workout\n4 minute jog\nJumping Jacks(1 minute x 4)\nMountain Climbers(1 minute x 4)\nSingle Leg V-Ups(1 minute x 4)\n1 minute Plank\nBurpees(1 minute x 4)\nBox Jumps(1 minute x 4)\nRussian Twists(1 minute x 4)','Light Cardio\nGo for a wallk or do Yoga','Full Body Strength Training\nLateral Pulldowns(4x12)\nPull Ups(4x8)\nUpright Row(3x12)\nTricep Extension(3x12)\nCable Squat(4x12)','Cardio (choose one of the following)\nWalk or Run 1 mile\nStairmaster fro 30 minutes\nBiking\nConsider one of the options above','Light Cardio (choose one of the following)\nGo for a wallk or do Yoga','Full Body Strength Training\nLateral Pulldowns(4x12)\nPull Ups(4x8)\nUpright Row(3x12)\nTricep Extension(3x12)\nCable Squat(4x12)'],
    'Gain Weight': ['Chest and Triceps\nBarbell Bench Press(4x12)\nIncline Dumbell Press(3x10)\nCable Flyes(3x12)\nTricep Pushdowns(3x10)\nSkull Crushers(3x8)','Back and Biceps\nDeadlifts(4x8)\nPull-ups(3x8)\nBarbell Rows(3x8)\nPreacher Curls(3x10)\nHammer Curls(3x10)','Rest','Legs and Shoulders\nSquats(4x10)\nLeg Press(3x10)\nLeg Curls(3x12)\nSeated Shoulder Press(4x8)\nLateral Raise(3x10)','Chest and Triceps\nBarbell Bench Press(4x12)\nIncline Dumbell Press(3x10)\nCable Flyes(3x12)\nTricep Pushdowns(3x10)\nSkull Crushers(3x8)','Back and Biceps\nDeadlifts(4x8)\nPull-ups(3x8)\nBarbell Rows(3x8)\nPreacher Curls(3x10)\nHammer Curls(3x10)','Rest'],
    'Body Recomposition': ['Upper Body\n5-10 minutes of light cardio to warm-up\nBench Press(3x10)\nRows(3x10)\nShoulder Press(3x10)\nLateral Pulldown(3x10)\nBicep Curls(3x10)\nTricep Extension(3x10)\nStretch to cool-down','Lower Body\n5-10 minutes of light cardio to warm-up\nSquats(3x10)\nDeadlifts(3x10)\nLunges(3x10)\nLeg Press(3x10)\nCalf raises(3x10)\nStretch to cool-down','Cardio\n30-45 minutes of one of the following:\nRunning\nBiking\nSwimming\nJogging','Upper Body\n5-10 minutes of light cardio to warm-up\nBench Press(3x10)\nRows(3x10)\nShoulder Press(3x10)\nLateral Pulldown(3x10)\nBicep Curls(3x10)\nTricep Extension(3x10)\nStretch to cool-down','Lower Body\n5-10 minutes of light cardio to warm-up\nSquats(3x10)\nDeadlifts(3x10)\nLunges(3x10)\nLeg Press(3x10)\nCalf raises(3x10)\nStretch to cool-down','Cardio\n30-45 minutes of one of the following:\nRunning\nBiking\nSwimming\nJogging','Rest']
}

class Exercises:
    def __init__(self, name,exercises,category):
        self.name = name
        self.exercises = exercise_presets[category]

    def get_exercises(self):
        return self.exercises
    
    def workoutPlan(user_info):
        if user_info.goal == 'Body Recomposition':
            workout_plan = exercise_presets['Body Recomposition']
        elif user_info.goal == 'Lose Weight':
            workout_plan = exercise_presets['Lose Weight']
        elif user_info.goal == 'Gain Weight':
            workout_plan = exercise_presets['Gain Weight']
        else:
            print('Sorry, we could not recommend a workout plan for this specific goal.')

        print('Based off of this information, your recommended workout plan is:')
        for day in range(user_info.days):
            print(f'Day {day+1}: {workout_plan[day%len(workout_plan)]}')

#call the exercise class and display the recommended workput plan for them
Exercises.workoutPlan(u1)
