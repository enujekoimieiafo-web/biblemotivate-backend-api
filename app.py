import random
from flask import flask,jsonify
from flask_cors import CORS 
# 100 Motivation Notes with Bible Verses
motivation_notes = [
    # Faith & Strength
    "You are stronger than your storm. Keep going. [Philippians 4:13]",
    "God hasn't brought you this far to leave you now. [Deuteronomy 31:6]",
    "When you feel weak, His strength carries you. [Isaiah 40:31]",
    "Faith is taking the first step even when you can't see the stairs. [Hebrews 11:1]",
    "You are not alone in the fight. [Joshua 1:9]",

    # Purpose & Calling
    "You were created for a reason. Walk in it. [Jeremiah 29:11]",
    "Your purpose is bigger than your pain. [Romans 8:28]",
    "God has plans to give you hope and a future. [Jeremiah 29:11]",
    "You are chosen, not by accident. [1 Peter 2:9]",
    "Your life is a masterpiece in progress. [Ephesians 2:10]",

    # Mindset & Growth
    "Renew your mind and your life will change. [Romans 12:2]",
    "Growth starts where comfort ends. [James 1:2-4]",
    "Think big. God can do exceedingly abundantly. [Ephesians 3:20]",
    "You become what you think about most. [Proverbs 23:7]",
    "Progress, not perfection, is the goal. [Philippians 1:6]",

    # Hard Work & Discipline
    "Whatever you do, work at it with all your heart. [Colossians 3:23]",
    "Diligence leads to success. Laziness leads to lack. [Proverbs 10:4]",
    "Small daily steps lead to big results. [Zechariah 4:10]",
    "Your work is seen by God. Do it well. [Colossians 3:23]",
    "Discipline is choosing between what you want now and what you want most. [1 Corinthians 9:25]",

    # Patience & Timing
    "Wait on the Lord. Your time is coming. [Psalm 27:14]",
    "God's timing is never late, never early. [Ecclesiastes 3:1]",
    "Be patient. Great things take time. [Galatians 6:9]",
    "Rest in the process. God is working behind the scenes. [Psalm 46:10]",
    "Do not despise small beginnings. [Zechariah 4:10]",

    # Fear & Anxiety
    "Do not fear, for God is with you. [Isaiah 41:10]",
    "Be anxious for nothing, pray about everything. [Philippians 4:6]",
    "Fear has no place where faith lives. [2 Timothy 1:7]",
    "Cast all your worries on Him. [1 Peter 5:7]",
    "Peace is your portion. [John 14:27]",

    # Hope & Encouragement
    "This season will not last forever. [Psalm 30:5]",
    "Hope does not disappoint. [Romans 5:5]",
    "Joy comes in the morning. [Psalm 30:5]",
    "You are closer than you think. [Galatians 6:9]",
    "Keep your eyes on the prize. [Hebrews 12:1]",

    # Self-Worth & Identity
    "You are fearfully and wonderfully made. [Psalm 139:14]",
    "You are a child of God. [1 John 3:1]",
    "You are accepted, loved, and enough. [Ephesians 1:6]",
    "Your value is not in likes, but in Christ. [1 Corinthians 6:20]",
    "You are redeemed. [Ephesians 1:7]",

    # Wisdom & Decisions
    "If you lack wisdom, ask God. [James 1:5]",
    "Trust God, not just your understanding. [Proverbs 3:5-6]",
    "Wisdom is better than gold. [Proverbs 16:16]",
    "Seek first His kingdom. [Matthew 6:33]",
    "A wise person listens and learns. [Proverbs 19:20]",

    # Relationships & Love
    "Love is patient, love is kind. [1 Corinthians 13:4]",
    "Forgive as you have been forgiven. [Colossians 3:13]",
    "Speak life to others. [Proverbs 18:21]",
    "Iron sharpens iron. Choose good friends. [Proverbs 27:17]",
    "Above all, love deeply. [1 Peter 4:8]",

    # Provision & Money
    "God will supply all your needs. [Philippians 4:19]",
    "Give, and it shall be given to you. [Luke 6:38]",
    "The Lord is your shepherd, you shall not want. [Psalm 23:1]",
    "Work hard and be generous. [Proverbs 11:25]",
    "God owns it all. Be a good steward. [Psalm 24:1]",

    # Health & Rest
    "Your body is a temple. Take care of it. [1 Corinthians 6:19-20]",
    "Come to Him and find rest. [Matthew 11:28]",
    "Be strong in body, mind, and spirit. [3 John 1:2]",
    "Sleep is a gift from God. [Psalm 127:2]",
    "He heals all your diseases. [Psalm 103:3]",

    # Leadership & Influence
    "Lead by serving others. [Mark 10:44]",
    "Your light should shine before men. [Matthew 5:16]",
    "Be a voice, not an echo. [Isaiah 6:8]",
    "Influence starts with integrity. [Proverbs 11:1]",
    "God raises up leaders for such a time as this. [Esther 4:14]",

    # Creativity & Vision
    "You are created in the image of a Creator. [Genesis 1:27]",
    "Write the vision and make it plain. [Habakkuk 2:2]",
    "Dream big. God gives dreams. [Joel 2:28]",
    "Innovate for a purpose. [Exodus 35:31]",
    "Start before you feel ready. [Ecclesiastes 11:4]",

    # Overcoming Failure
    "A righteous man falls 7 times and rises. [Proverbs 24:16]",
    "Your past does not define your future. [Isaiah 43:18]",
    "Get up one more time than you fall. [Micah 7:8]",
    "Failure is feedback, not final. [Romans 8:37]",
    "God restores what was lost. [Joel 2:25]",

    # Gratitude & Joy
    "In everything, give thanks. [1 Thessalonians 5:18]",
    "Rejoice in the Lord always. [Philippians 4:4]",
    "Gratitude turns what you have into enough. [Psalm 100:4]",
    "This is the day the Lord has made. [Psalm 118:24]",
    "Count your blessings daily. [Psalm 103:2]",

    # Courage & Action
    "Be strong and very courageous. [Joshua 1:9]",
    "God did not give you a spirit of fear. [2 Timothy 1:7]",
    "Step out. Faith requires movement. [Matthew 14:29]",
    "Courage is faith in action. [Deuteronomy 31:6]",
    "You can do hard things with God. [Philippians 4:13]",

    # Focus & Priorities
    "Fix your eyes on Jesus. [Hebrews 12:2]",
    "One thing I do: press forward. [Philippians 3:13]",
    "Guard your heart above all else. [Proverbs 4:23]",
    "Do not be conformed to this world. [Romans 12:2]",
    "Seek things above, not earthly things. [Colossians 3:1]",

    # Community & Service
    "Serve one another in love. [Galatians 5:13]",
    "You are part of one body. [1 Corinthians 12:27]",
    "Bear one another’s burdens. [Galatians 6:2]",
    "Do good to all people. [Galatians 6:10]",
    "It is more blessed to give than to receive. [Acts 20:35]",

    # Perseverance & Finishing Well
    "Run with endurance the race set before you. [Hebrews 12:1]",
    "Do not grow weary in doing good. [Galatians 6:9]",
    "He who began a good work will complete it. [Philippians 1:6]",
    "Finish strong. [2 Timothy 4:7]",
    "Your latter days will be greater. [Job 8:7]",

    # Peace & Rest in God
    "Be still and know that He is God. [Psalm 46:10]",
    "The Lord gives peace to His people. [Psalm 29:11]",
    "Let the peace of Christ rule your heart. [Colossians 3:15]",
    "In quietness and trust is your strength. [Isaiah 30:15]",
    "He leads you beside still waters. [Psalm 23:2]"
]
motivate=random.choice(motivation_notes)
CORS(app)
app=Flask(__name__)
@app.route("/motivate")
def motivate():
	return jsonify (motivate)
if __name__ == "__main__":
	app.run(debug=True)
