#########################################
##### Name: SHAO-WEN CHANG #####
##### Uniqname: shaowenc   #####
#########################################


import unittest
import hw5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        c_q1 = hw5_cards.Card(rank = 12)
        X = Y = self.assertEqual(c_q1.rank_name, "Queen")
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''
        return X, Y

    def test_q2(self):
        c_q2 = hw5_cards.Card(suit = 1)
        X = Y = self.assertEqual(c_q2.suit_name, "Clubs")
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''
        return X, Y    
    

    def test_q3(self):
        c_q3 = hw5_cards.Card(3, 13)
        X = Y = self.assertEqual(c_q3.__str__(), "King of Spades")
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''
        return X, Y
    
    def test_q4(self):
        c_q4 = hw5_cards.Deck()
        X = Y = self.assertEqual(len(c_q4.cards), 52)
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''
        return X, Y  

    def test_q5(self):
        q5 = hw5_cards.Deck()
        X = Y = q5.deal_card()
        
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''
        return X, Y
    
    def test_q6(self):
        q6 = hw5_cards.Deck()
        q6.deal_card()
        X = Y = self.assertEqual(len(q6.cards), 51)
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''
        return X, Y    
    

    def test_q7(self):
        q7 = hw5_cards.Deck()
        last_card = q7.deal_card()
        q7.replace_card(card = last_card)
        X = Y = self.assertEqual(len(q7.cards), 52)

        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''
        
        return X, Y
    
    def test_q8(self):
        q8_1 = hw5_cards.Deck()
        last_card = q8_1.deal_card()
        q8_1.replace_card(card = last_card)

        q8_2 = hw5_cards.Deck()
        q8_2.replace_card(card = last_card)

        X = Y = self.assertEqual(len(q8_1.cards), len(q8_2.cards))

        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.
        '''
        return X, Y  



if __name__=="__main__":
    unittest.main()