package dk.danskdelight.item;

import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;

/**
 * En ret man kan spise. Hvis retten har en "craftRemainder" (fx en skål),
 * får spilleren den tilbage efter måltidet - ligesom Farmer's Delight's retter.
 */
public class MealItem extends Item {

    public MealItem(Properties properties) {
        super(properties);
    }

    @Override
    public ItemStack finishUsingItem(ItemStack stack, Level level, LivingEntity entity) {
        // Skal hentes FØR stakken skrumper (en tom stak har ingen "rest")
        ItemStack remainder = stack.getCraftingRemainingItem();
        ItemStack result = super.finishUsingItem(stack, level, entity);

        if (remainder.isEmpty()) {
            return result;
        }
        if (entity instanceof Player player && player.getAbilities().instabuild) {
            return result;
        }
        if (result.isEmpty()) {
            return remainder;
        }
        if (entity instanceof Player player && !player.getInventory().add(remainder)) {
            player.drop(remainder, false);
        }
        return result;
    }
}
