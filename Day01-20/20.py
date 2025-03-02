import random

class Card:
    """单张扑克牌"""
    SUITS = ['♠', '♥', '♦', '♣']
    RANKS = ['A', '2', '3', '4', '5', '6', '7', 
             '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @property
    def value(self):
        """获取牌面"""
        if self.rank in ['J', 'Q', 'K']:
            return 10
        if self.rank == 'A':
            return 11 # 后续处理动态调整
        return int(self.rank)
    
    def __repr__(self):
        return f"{self.suit}{self.rank}"
        
class Deck:
    """牌堆管理"""
    # def __init__(self):
    #     self.cards = [
    #         Card(suit, rank)
    #         for suit in Card.SUITS
    #         for rank in Card.RANKS
    #     ]
    #     random.shuffle(self.cards)

    def __init__(self, num_decks=1, include_jokers=False):  # 添加参数
        self.cards = []
        # 生成多副牌
        for _ in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    self.cards.append(Card(suit, rank))
            if include_jokers:
                self.cards.extend([Card('★', 'Joker'), Card('☆', 'Joker')])
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

class Hand:
    """手牌管理及点数计算"""
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
    
    @property
    def value(self):
        """动态计算手牌点数（智能处理A）"""
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total
    
    def __repr__(self):
        return ", ".join(map(str,self.cards))


    
class Player:
    """玩家基类"""
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.is_stand = False

    def hit(self, deck):
        self.hand.add_card(deck.draw())
        print(f"{self.name}要牌 → 手牌：{self.hand}")

    def stand(self):
        self.is_stand = True
        print((f"{self.name} 选择停牌"))

    def show_hand(self, show_all=False):
        """庄家隐藏第一张牌"""
        if isinstance(self, Dealer) and not show_all:
            return f"{self.hand.cards[0]}, [?]"
        return str(self.hand)
    
class HumanPlayer(Player):
    """人类玩家"""
    def make_decision(self):
        while True:
            choice = input("要牌(h)还是停牌(s)? ").lower()
            if choice in ['h', 's']:
                return choice
            print("输入错误，请重新选择")
    
class Dealer(Player):
    """庄家（自动逻辑）"""
    def auto_play(self, deck):
        """庄家自动要牌逻辑"""
        while self.hand.value < 17:
            self.hit(deck)


class Game:
    """游戏流程控制"""
    def __init__(self):
        self.deck = Deck()
        self.player = HumanPlayer("玩家")
        self.dealer = Dealer("庄家")

    def initial_deal(self):
        """初始发牌"""
        for _ in range(2):
            self.player.hand.add_card(self.deck.draw())
            self.dealer.hand.add_card(self.deck.draw())
        
    # def player_turn(self):
    #     """玩家回合"""
    #     while not self.player.is_stand and self.player.hand.value <= 21:
    #         print(f"\n你的手牌：{self.player.hand}，当前点数：{self.player.hand.value}")
    #         print(f"庄家手牌：{self.dealer.show_hand()}")
            
    #         if self.player.make_decision() == 'h':
    #             self.player.hit(self.deck)
    #             if self.player.hand.value > 21:
    #                 print("爆牌了！")
    #                 return
    #         else:
    #             self.player.stand()
    
    def player_turn(self):
        """玩家回合"""
        while not self.player.is_stand and self.player.hand.value <= 21:
            # 步骤1：显示当前牌局信息
            print(f"\n你的手牌：{self.player.hand}，当前点数：{self.player.hand.value}")
            print(f"庄家手牌：{self.dealer.show_hand()}")  # 显示庄家第一张牌和隐藏牌
            
            # 步骤2：获取玩家决策
            if self.player.make_decision() == 'h':
                # 步骤3a：要牌操作
                self.player.hit(self.deck)
                # 步骤4：爆牌检测
                if self.player.hand.value > 21:
                    print("爆牌了！")
                    return  # 直接结束玩家回合
            else:
                # 步骤3b：停牌操作
                self.player.stand()
    
    def dealer_turn(self):
        """庄家回合"""
        print(f"\n庄家手牌：{self.dealer.hand}，当前点数：{self.dealer.hand.value}")
        self.dealer.auto_play(self.deck)
    
    def show_result(self):
        """显示最终结果"""
        p_value = self.player.hand.value
        d_value = self.dealer.hand.value
        
        print("\n最终结果：")
        print(f"你的手牌：{self.player.hand} → {p_value}")
        print(f"庄家手牌：{self.dealer.hand} → {d_value}")
        
        if p_value > 21:
            print("你爆牌了，庄家获胜！")
        elif d_value > 21:
            print("庄家爆牌，你赢了！")
        elif p_value > d_value:
            print("你赢了！")
        elif p_value < d_value:
            print("庄家获胜！")
        else:
            print("平局！")
    
    def play(self):
        self.initial_deal()
        self.player_turn()
        if self.player.hand.value <= 21:
            self.dealer_turn()
        self.show_result()

# 运行游戏
if __name__ == "__main__":

    """
    21点规则要点：
   玩家和庄家初始各发2张牌
   J/Q/K计10点，A可计1或11点
   玩家先行动：要牌（Hit）或停牌（Stand）
   玩家爆牌（>21点）立即输
   庄家必须要牌直到点数≥17
   最后比较点数，大者胜（需≤21点）
    """

    while True:
        print("输入任意键开始，Q/q退出,")
        end = input()
        if end != 'Q' and end != 'q':
            Game().play()
        else:
            break
        
    