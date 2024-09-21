

# 10 * 9 * 8 = 720通り
# 計算量考える必要なし
# おすすめの手を表示する
# 3桁の場合 パターン
# 1. 3E 0B　
# 2. 2E 0B
# 3. 1E 0B

# 4. 1E 1B
# 5. 0E 0B

# 6. 0E 1B
# 7. 0E 2B
# 8. 1E 2B
# 9. 0E 3B


# 相手の数字が813

# 012 -> 1E0B
# 0,1,2の中に必ず正解がある

# a. 0が正解の場合
# 0 , (0,1,2以外の数字) , (0,1,2と二桁目の選択した数字以外) 1*7*6 

# b. 1が正解の場合
#  (0,1,2以外の数字) , 1 ,(0,1,2と二桁目の選択した数字以外) 

# c. 2が正解の場合 

# 124通り
import itertools
import copy

class Numeron():
  def __init__(self):
    self.candidates = [i for i in range(10)]
    self.initial_ans = []

    for n in range(len(self.candidates)):
      for m in range(len(self.candidates)):
        for l in range(len(self.candidates)):
          if n != m and n != l and m != l:
            self.initial_ans.append([self.candidates[n],self.candidates[m],self.candidates[l]])

  def pattern_1(self,index,array,temp_candidates):
    # arrayのindex番目に値を入れる
    return_data = []
    
    for num in  temp_candidates:
      data = []
      data = copy.copy(array)
      data.insert(index,num)
      return_data.append(data)
    return return_data 
  
  def pattern_2(self,index,num,temp_candidates):
    ans = []
    for num_A in  temp_candidates:
      for num_B in temp_candidates:
        if num_A != num_B:
          # 0番目のやつを1,2 で固定
          if index == 0:
            # print(num,num_A,num_B)
            ans.append([num,num_A,num_B])
          if index == 1:
            # print(num_A,num,num_B)
            ans.append([num_A,num,num_B])
          if index == 2:
            # print(num_A,num_B,num)
            ans.append([num_A,num_B,num])
          
    filter_ans = [a for a in ans if a in self.initial_ans]
    filter_ans.sort()

    return filter_ans

  def result_0E0B(self,predict,now_ans):
    # 候補の中の予想の数字が入ってるものを全て取り除く
    now_ans_without_predict = [ans for ans in now_ans if all(num not in ans for num in predict)]
    now_ans_without_predict.sort()
    return now_ans_without_predict

  def result_1E0B(self,predict,now_ans):
  # 0,1,2 の数字のどれかは正解
    filtered_candidates = [ num for num in self.candidates if num not in predict]

    ans = []
    for i in range(3):
      for n in range(len(filtered_candidates)):
        for m in range(len(filtered_candidates)):
            p_list = [filtered_candidates[n],filtered_candidates[m]]
            if n != m: 
              # i番目のpredict[i]
              p_list.insert(i,predict[i])
              
              ans.append(p_list)
    # 元の候補と現在の候補の共通部分のみにする
    filter_ans = [a for a in ans if a in now_ans]
    filter_ans.sort()
    return filter_ans
  




  # 813-> 1E1Bの場合
  # 8が正解の場合
  # -> 3が位置違い 83?
  # -> 1が位置違い 8?1

  # 1が正解の場合
  # -> 8が位置違い ?18
  # -> 3が位置違い 31?

  # 3が正解の場合
  # -> 8が位置違い ?83
  # -> 1が位置違い 1?3
  # 3 * (10 - 3) = 21


    # 間違えてる
  def result_1E1B(self,predict,now_ans):
    filtered_candidates = [ num for num in self.candidates if num not in predict]

    ans = []
    # ここ書き直す
    for i in range(3):
      for j in range(3):
        for k in range(len(filtered_candidates)):
          # 1番目が正解の場合
          if i == 0:
            # 2番目が位置違いの場合
            if j == 1:
              ans.append([predict[i],filtered_candidates[k],predict[j]])
              # print(predict[i],"X",predict[j])
              
            # 3番目が位置違いの場合
            if j == 2:
              ans.append([predict[i],predict[j],filtered_candidates[k]])
              # print(predict[i],predict[j],"X")
          # 2番目が正解の場合
          if i == 1:
            # 1番目が位置違いの場合
            if j == 0:
              # print("X",predict[i],predict[j])
              ans.append([filtered_candidates[k],predict[i],predict[j]])
            # 3番目が位置違いの場合
            if j == 2:
              # print(predict[j],predict[i],"X")
              ans.append([predict[j],predict[i],filtered_candidates[k]])
          # 3番目が正解の場合
          if i == 2:
            # 1番目が位置違いの場合
            if j == 0:
              # print("X",predict[j],predict[i])
              ans.append([filtered_candidates[k],predict[j],predict[i]])
            # 2番目が一違いの場合
            if j == 1:
              # print(predict[j],"X",predict[i])
              ans.append([predict[j],filtered_candidates[k],predict[i]])

    filter_ans = [a for a in ans if a in now_ans]
    filter_ans.sort()
    return filter_ans

  # 813 -> 0E1Bの場合
  # 1番目が位置違い
  # -> ?8?
  # -> ??8
  # 2番目が位置違い
  # -> 1??
  # -> ??1 
  # 3番目が位置違い
  # -> 3??
  # -> ?3?


  def result_0E1B(self,predict,now_ans):
    filtered_candidates = [ num for num in self.candidates if num not in predict]
    ans = []
    
    for i in range(3):
      if i == 0:
        # print("X","X",predict[i])
        # print("X",predict[i],"X")
        ans+=self.pattern_2(2,predict[i],filtered_candidates)
        ans+=self.pattern_2(1,predict[i],filtered_candidates)
        
      if i == 1:
        # print(predict[i],"X","X")
        # print("X","X",predict[i])
        ans+=self.pattern_2(0,predict[i],filtered_candidates)
        ans+=self.pattern_2(2,predict[i],filtered_candidates)
      if i == 2:
        # print(predict[i],"X","X")
        # print("X",predict[i],"X")
        ans+=self.pattern_2(0,predict[i],filtered_candidates)
        ans+=self.pattern_2(1,predict[i],filtered_candidates)

    filter_ans = [a for a in ans if a in now_ans]
    filter_ans.sort()
    return filter_ans

  
  def result_0E2B(self,predict,now_ans):

      # 012 -> 0E2Bの場合
      # 1番目が違う場合
      # 12?
      # 2?1
      # ?21
      # 2番目が違う場合
      # 20? 
      # 2?0
      # ?20

      # 3番目が違う場合
      # 10?
      # 1?0
      # ?01


    filtered_candidates = [ num for num in self.candidates if num not in predict]
    ans = []
    for k in range(len(filtered_candidates)):
      # 0が間違えの場合
      ans.append([predict[1],predict[2],filtered_candidates[k]])      
      ans.append([predict[2],filtered_candidates[k],predict[1]])      
      ans.append([filtered_candidates[k],predict[2],predict[1]])
      
      ans.append([predict[2],predict[0],filtered_candidates[k]])      
      ans.append([predict[2],filtered_candidates[k],predict[0]])        
      ans.append([filtered_candidates[k],predict[2],predict[1]])   

      ans.append([predict[1],predict[0],filtered_candidates[k]])      
      ans.append([predict[1],filtered_candidates[k],predict[0]])      
      ans.append([filtered_candidates[k],predict[0],predict[1]])    

    ans = list(map(list, set(map(tuple, ans))))

    filter_ans = [a for a in ans if a in now_ans]
    filter_ans.sort()
    return filter_ans


  def result_0E3B(self,predict,now_ans):
    ans = []
    for i in range(3):
      for j in range(3):
        for k in range(3):
          # 3つの数字が同じでない　
          if i != j and j != k  and i != k:
            # 数字が予想の場所と同じ場所でない
            if predict[0] == predict[i] or predict[1] == predict[j] or predict[2] == predict[k]:
              continue
            ans.append([predict[i] , predict[j], predict[k]])

    filter_ans = [a for a in ans if a in now_ans]
    filter_ans.sort()
    return filter_ans


  def result_1E2B(self,predict,now_ans):
    ans = []
    for i in range(3):
        for j in range(3):
          for k in range(3):
            # 3つの数字が同じでない　
            if i != j and j != k  and i != k:
              # predict[i]が正解の場合
              if i == 0 and [predict[i],predict[j],predict[k]] != predict:
                ans.append([predict[i],predict[j],predict[k]])
              if i == 1 and [predict[j],predict[i],predict[k]] != predict:      
                ans.append([predict[j],predict[i],predict[k]])
              if i == 2 and [predict[k],predict[j],predict[i]] != predict:
                ans.append([predict[k],predict[j],predict[i]])     

    filter_ans = [a for a in ans if a in now_ans]
    filter_ans.sort()
    return filter_ans


  def result_2E0B(self,predict,now_ans):
    value = [ num for num in self.candidates if num not in predict]
    for i in predict:
      if i in value:
        value.remove(i)
    list_data = list(itertools.permutations(predict,2))
    ans = []
    for l in list_data:
      for i in value:
        for j in range(3):
          # j番目にiをくわえわえる
          data = list(l)
          data.insert(j,i)
          ans.append(data)
    
    filter_ans = [a for a in ans if a in now_ans]
    filter_ans.sort()
    return filter_ans

  def mini_max(self,predict):
    # 予想の中からおすすめの選択肢を返す
    pass


  def is_number(self,num):
    try: 
      int(num)
      return True
    except:
      return False

  def is_xxx(self,num):
    num = str(num)
    if num == 3: 
      return True
    return False
