export let branches = [
  {
    modid: "enderutilities",
    key: "item.enderutilities.handybag.tooltips",
    zh_cn:
      "- 打开物品栏时这个背包会被打开|lf  物品栏里可以看到手提包|lf- The first bag found (= hotbar first,|lf  then top-left-most first) will be used.|lf- Sneak while opening the inventory to|lf  open the regular inventory instead.|lf- 模式键: 切换拾取模式|lf- Shift+模式键: 切换锁定状态|lf  (锁定的背包不会随着物品栏打开)|lf- Alt+Shift+模式键: 切换重装模式|lf- Alt+模式键: 切换公共/私有属性|lf  (注意: 它的存储单元是每个内存卡!)|lf- Uses item type Memory Cards|lf- 最高堆叠数取决于使用的内存卡的等级|lf- 一般的背包有27格空间, 大型背包有55格|lf- 提示: 中键可互换两格中的物品"
  },
  {
    modid: "industrialwires",
    key: "ie.manual.entry.industrialwires.marx",
    zh_cn:
      "马克思发电机是一种用于产生高压高能脉冲的装置。这些脉冲在输出端子之间是像闪电一样可见的，可用于处理矿石。每种矿石都有理想的加工能量（参见<link;industrialwires.marx;§oAppendix B§r;7>）。准确值是未知的, 10%%的准确性的估计值可以在这个条目的末尾找到。对所有类型的矿石来说，实际值与估算之间的系数是相同的。<br>§l建造§r<&0><br>上述方案显示了一个能够产生3个方块闪电的5层发电机。可以通过增加“中间”层数来增加任意的级数。电源（IF或EU）连接到高压接线器，控制信号的红石线连接到红石接线器。<br>§l能量§r<br>马克思发电机的每层由一个充电到250 kV的1.6 μF电容器组成，（参见<link;industrialwires.marx;§oAppendix A§r;6>）。当发电机完全充电时, 每个电容器的电压大致等于充电电压。总能量是存储在单独电容器中的能量的总和，在要加工的矿石之间平分。<br> §l控制信号§r<br>电压由两个信号表示：第一个信号与所表示的电压成正比。第二个信号与和第一个信号之间“差距”两个值的电压成正比，从而允许更精确的控制/测量。能够与模拟信号进行交互的面板组件通常支持这种双通道设置。充电电压由白色和黄色信号控制。顶部和底部电容器的电压输出到品红色和粉红色分别为橙色和黄绿色的信号。淡蓝色信号是一个点火控制。如果它的信号高发电机将试图开火。如果底部电容器的电压低于125 kV或总电压低于最大输出电压的30%%，发电机将会失火，电容器会在没有实际产生闪电的情况下放电。<br>§l安全§r<br>由于激发马克思发电机所涉及的高电压和能量，应保持安全距离，以避免造成伤害或死亡。甚而在这个区域外面听力保护（由沉浸式工程提供）是强制的。计算安全距离的公式可以在<link;industrialwires.marx;§oAppendix A§r;6>中找到。<np>§l附录A：公式§r<br>存储在电容器中的能量：<br>E=0.5*U^2<br>E：能量，C：电容, U：电压<br><br>来自红石信号的电压：<br>U=250/255*(16*A+b)<br>U：电压（kV），A：第一信号，b：第二信号<br><br>安全距离（物理损失））：<br>r=sqrt(e/50000)<br>r：安全距离，e：已存储能量<br><br>安全距离（听力损伤）：<br>r=sqrt(e)/50<br>r：安全距离，e：已存储能量<np>§l附录B：矿物能量值§r<br>"
  },
  {
    modid: "nuclearcraft",
    key: "gui.config.tools.tool_attack_damage.comment",
    zh_cn:
      "于每次攻击的伤害有关 (木质 = 0.0, 石制 = 1.0, etc.). 顺序: 硼, 硼镐尖斧, 高强合金, 高强合金镐尖斧, 硬碳合金, 硬碳镐尖斧, 氮化硼, 氮化硼镐尖斧。"
  },
  {
    modid: "nuclearcraft",
    key: "gui.config.tools.tool_mining_level.comment",
    zh_cn:
      "挖掘等级 (木制 = 0, 石制 = 1, etc.). 顺序: 硼, 硼镐尖斧, 高强合金, 高强合金镐尖斧, 硬碳合金, 硬碳镐尖斧, 氮化硼, 氮化硼镐尖斧。"
  },
  {
    modid: "nuclearcraft",
    key: "gui.config.tools.tool_speed.comment",
    zh_cn:
      "决定挖掘方块的速度 (木制= 2.0, 石制 = 4.0, etc.). 顺序: 硼, 硼镐尖斧, 高强合金, 高强合金镐尖斧, 硬碳合金, 硬碳镐尖斧, 氮化硼, 氮化硼镐尖斧。"
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.info.item.drone.dispenserUpgrade",
    zh_cn:
      "§0By default the Drone can transfer one stack of items. For every Dispenser Upgrade inserted, the Drone can transfer one additional stack. \\n \\nIt will also increase the internal liquid tank by 16000mB per upgrade, and 100000RF storage per upgrade (if installed). It also increases the rate at which the Drone can transfer RF (transfer = max storage / 100)."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.advanced_air_compressor",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0The Advanced Air Compressor will produce more compressed air per tick. However this is at the expense of the efficiency."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.advanced_liquid_compressor",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0Increases the compressed air generated per tick. However this is at the expense of the efficiency. \\n§7-Dispenser Upgrade (max = 1) \\n§0The Liquid hopper will try to pump in any liquid block at the input side. Likewise it'll try to place any liquid in the world on the output side (if it's an air block)."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.air_cannon",
    zh_cn:
      "§7-Dispenser Upgrade \\n§0Will make the cannon act like a Dispenser. Any item that would act special in a Dispenser, will be handled the same way in here. \\n§7-Entity Tracker Upgrade (max = 5) \\n§0When fired, the Air Cannon will grab the closest living entity and shoot it to the set coordinate. This can be used as player transport. It has a grabbing radius of 1 by default. Per inserted Entity Tracker Upgrade the radius will increase by one. \\n§7-Block Tracker Upgrade \\n§0When fired, items being shot automatically will try to go into inventories they hit. When firing at a Chest for example, items will land in the Chest without needing a Hopper. \\n§7-Item Life Upgrade \\n§0By default the Air Cannon shoots items which have a lifespan of 60 seconds. For each of this upgrades you put in you get an additional 30 seconds. \\n§7-Speed Upgrade (max = 10) \\n§0The cannon will turn faster. \\n§7-Range Upgrade \\n§0The shooting range will increase by about 25 blocks per upgrade, up to 250 blocks."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.air_compressor",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0The Air Compressor will produce more compressed air per tick. However this is at the expense of the efficiency."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.assembly_controller",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0All assembly machines that are controlled by this Controller will operate faster."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.charging_station",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0The Charging Station will be able to (dis)charge items faster. \\n§7-Dispenser Upgrade \\n§0Adds a charge pad onto the Charging Station, allowing it to (dis)charge any Drones, items, and player inventory items that are on top of the Charging Station."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.elevator_base",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0The elevator will ascend/descent faster (at a higher energy cost)."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.flux_compressor",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0Increases the air production rate. It also increases the RF usage in a way that the machine will be more inefficient. Finally it increases the max RF input rate."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.gas_lift",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0Increases the pumping/digging/retracting rate. \\n§7-Dispenser Upgrade (max = 1) \\n§0The Gas Lift will auto-eject liquids into adjacent tanks."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.liquid_compressor",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0Increases the compressed air generated per tick. However this is at the expense of the efficiency."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.liquid_hopper",
    zh_cn:
      "§7-Speed Upgrade (max = 13) \\n§0Increases the speed at which the Hopper transfers liquid. \\n§7Dispenser Upgrade \\n§0Sucks any liquid block at the input side of the Hopper, and places down any liquid at the output side. Can be used for example as water pump."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.omnidirectional_hopper",
    zh_cn:
      "§7-Speed Upgrade (max = 13) \\n§0Increases the speed at which the Hopper transfers items."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.pneumatic_dynamo",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0Increases the RF production rate. It also increases the air usage in a way that the machine will be more inefficient. Finally it increases the max RF output rate."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.pressure_chamber_interface",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0The floodgates of the Interface will open/close faster, meaning items can be transported quicker."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.programmable_controller",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0Increases the travel speed of the Drone. \\n§7-Dispenser Upgrade (max = 35) \\n§0By default the Drone can transfer one stack of items. For every Dispenser Upgrade inserted, the Drone can transfer one additional stack. \\n \\nIt will also increase the internal liquid tank by 16000mB per upgrade, and 100000RF storage per upgrade (if installed). It also increases the rate at which the Drone can transfer RF (transfer = max storage / 100)."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.sentry_turret",
    zh_cn:
      "§7-Range Upgrade (max = 16) \\n§0Increases the range of the Sentry Turret by one for each upgrade."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.thermopneumatic_processing_plant",
    zh_cn:
      "§7-Dispenser Upgrade (max = 1) \\n§0The Thermopneumatic Processing Plant will auto-eject liquids into adjacent tanks."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.uv_light_box",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0The UV lights will glow brighter and will expose PCB's quicker."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.tab.upgrades.tile.vacuum_pump",
    zh_cn:
      "§7-Speed Upgrade (max = 10) \\n§0The Vacuum Pump will produce more vacuum per tick. However this is at the expense of the efficiency."
  },
  {
    modid: "pneumaticcraft",
    key: "gui.universalSensor.desc.playerHealth",
    zh_cn:
      "This sensor option emits a redstone signal proportional to the player's health. no health = 0, max health = 15, and anything in between. The player's name needs to be put into the textbox."
  },
  {
    modid: "smoothfont",
    key: "smoothfont.msg.detectFastCraft",
    zh_cn:
      "检测到Fastcraft，请在fastcraft.ini中设定为enableFontRendererTweaks=false"
  },
  {
    modid: "technom",
    key: "techno.research_page.NODEGENERATOR.3",
    zh_cn:
      "<LINE>创造: 如果没有节点，他们依据所处的环境会吸取腐化和灵气源质进入储存，吸取的种类可以通过制造器的闪电球颜色判别。 然后，只需要简单的用法杖右击其中一个创造器，然后两个生成器都会消耗全部存储的源质并且被右击的生成器会从抽取内部能量存储((((Aurum+Taint)/2)^2)*762.939453125 = Energy(RF))的能量。生成节点的大小为总吸收的源质总数的一半，节点的种类和等级由和污染的比例和源质总量决定,节点的要素种类取决于所处的生物群系. 需要注意的是, 在一侧注入过量源质并不会很好地生成一个过大或是过小的节点。"
  }
];
