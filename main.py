import sys


def main():
  try:
    print("Welcomg to the game!")

    #check for user agreement
    user_input = input("Are you ready to start? (yes/no)\n")
    if user_input.lower() == "no":
      print("Sad to see you go. Stopping the game.")
      exit_program()
    elif user_input.lower() != "yes":
      print("Invalid option. This is not yes/no.")
      exit_program()
    else:
      pass  # User said yes, continue with the game
  except Exception as message:
    print(f"An error occured: {message}")
    exit_program()


def exit_program():
  print("Exiting program...")
  #zero as the argument/exit code for function
  sys.exit(0)


#the check if the script is being executed as the main module
if __name__ == "__main__":
  main()

print("Once upon a time...")


class TreeNode:

  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)

    while len(story_node.choices) > 0:
      choice = input("Enter 1 or 2 to continue the story: \n")
      if choice not in ["1", "2"]:
        print("Please, enter a valid choice: ")
      else:
        chosen_index = int(choice)
        chosen_index -= 1
        chosen_child = story_node.choices[chosen_index]
        print(chosen_child.story_piece)
        story_node = chosen_child


story_root = TreeNode("""
You are in a forest. There is a path to the left.
A bear appears out of nowhere and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

choice_a = TreeNode("""
The bear is startled and just runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode("""
After turning to the left, you come across a clearing full of flowers. 
The bear followed you but now he starts talking; 'what is going on?, he asks you'
Do you:
1 ) Gasp 'Wow, a talking bear!'
2 ) Explain to him that he scared you, and that you are looking for an escape.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)
story_root.traverse()

choice_a_1 = TreeNode("""
The bear returns and he is talking. Wow, a talking bear! However, in the end, he helps you and shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2 = TreeNode("""
The bear returns roars one more time at you meanly, and then he leaves you alone
in the wilderness.

YOU REMAIN LOST.
""")

choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_a.traverse()

choice_b_1 = TreeNode("""
The bear is unamused by your remark. After smelling the flowers, he just turns around and leaves you alone.

YOU REMAIN LOST.
""")

choice_b_2 = TreeNode("""
The bear understands and apologizes for scaring you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
choice_b.traverse()

#print(story_root.story_piece)
#user_choice = input("What is your name?\n")
#print(user_choice)
